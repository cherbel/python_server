import logging

import tornado.web
import json

from aswwu.base_handlers import BaseHandler
import aswwu.alchemy as alchemy
import aswwu.models.elections as election_model

logger = logging.getLogger("aswwu")

election_db = alchemy.election_db


# get all of the profiles in our database
class AllElectionVoteHandler(BaseHandler):
    def get(self):
        votes = alchemy.query_all_election(election_model.Election)
        self.write({'results': [v.info() for v in votes]})


# update user's vote
class ElectionVoteHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self, username):
        user = self.current_user
        if user.username == username or 'administrator' in user.roles:
            usrvote = alchemy.query_by_wwuid_election(election_model.Election, str(user.wwuid))
            # Fix this to be more efficient
            if len(usrvote) == 0:
                new_vote = election_model.Election(wwuid=str(user.wwuid))
                vote = alchemy.add_or_update_election(new_vote)
            else:
                vote = election_db.query(election_model.Election).filter_by(wwuid=str(user.wwuid)).one()
            vote.candidate_one = self.get_argument('candidate_one', '')
            vote.candidate_two = self.get_argument('candidate_two', '')
            vote.sm_one = self.get_argument('sm_one', '')
            vote.sm_two = self.get_argument('sm_two', '')
            vote.new_department = self.get_argument('new_department', '')
            vote.district = self.get_argument('district', '')

            alchemy.add_or_update_election(vote)

            self.write({'vote': 'successfully voted'})
        else:
            self.write({'error': 'invalid voting permissions'})


class ElectionLiveFeedHandler(BaseHandler):
    def get(self):
        votes = alchemy.query_all_election(election_model.Election)
        self.write({'size': len(votes)})


class ElectionCandidateHandler(BaseHandler):
    def get(self, district):
        candidates = alchemy.query_district_election(district)
        self.write({
            'candidates': [c.to_json for c in candidates]
        })

    @tornado.web.authenticated
    def post(self, district):
        # variables
        user = self.current_user
        body = self.request.body.decode('utf-8')
        body_json = json.loads(body)
        # check authorization
        if 'election-admin' not in user.roles and 'administrator' not in user.roles:
            self.set_status(403)
            self.write({'status': 'insufficient permissions'})
        candidate = alchemy.query_candidate_election(str(body_json['username']))
        # Fix this to be more efficient
        if len(candidate) == 0:
            new_candidate = election_model.Candidate(username=str(body_json['username']))
        else:
            new_candidate = alchemy.query_candidate_election(username=str(body_json['username']))

        new_candidate.full_name = str(body_json['full_name'])
        new_candidate.district = str(district)

        alchemy.add_or_update_election(new_candidate)

