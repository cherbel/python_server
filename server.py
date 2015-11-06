
import os
import logging
import tornado.escape
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.options import define, options

from alchemy.base_handlers import *
from alchemy.search_handlers import *

from alchemy.form_handlers import *
from alchemy.role_handlers import *
from alchemy.volunteer_handlers import *

from alchemy.old_db_handlers import *

define("port", default=8888, help="run on the given port", type=int)
define("log_name", default="aswwu", help="name of the logfile")
define("auth_url", default="https://aswwu.com/auth")
define("current_year", default="1516")


class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            "login_url": "/login"
        }

        handlers = [
            (r"/form", FormHandler),
            (r"/form/(.*)", FormHandler),
            (r"/question", QuestionHandler),
            (r"/question/(.*)", QuestionHandler),
            (r"/answer", AnswerHandler),
            (r"/answer/(.*)", AnswerHandler),
            (r"/login", LoginHandler),
            (r"/old_db", LookUpOldHandler),
            (r"/profile/(.*)/(.*)", ProfileHandler),
            (r"/profile_photo/(.*)/(.*)", ProfilePhotoHandler),
            (r"/role/administrator", AdministratorRoleHandler),
            (r"/role/volunteer", VolunteerRoleHandler),
            (r"/search/all", ListProfilesHandler),
            (r"/search/(.*)/(.*)", SearchHandler),
            (r"/update/(.*)", UpdateProfileHandler),
            (r"/volunteer", VolunteerHandler),
            (r"/volunteer/(.*)", VolunteerHandler),
            (r"/verify", VerifyLoginHandler),
            (r"/", IndexHandler),
        ]

        self.options = options
        logger = logging.getLogger(options.log_name)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("etc/logs/"+options.log_name+".log")
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter("{'timestamp': %(asctime)s, 'loglevel' : %(levelname)s %(message)s }")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        tornado.web.Application.__init__(self, handlers, **settings)
        logger.info("Application started on port " + str(options.port))


if __name__ == "__main__":
    config = tornado.options.parse_command_line()
    if len(config) == 0:
        conf_name = "default"
    else:
        conf_name = config[0]
    io_loop = tornado.ioloop.IOLoop.instance()
    tornado.options.parse_config_file("etc/conf/"+conf_name+".conf")
    application = Application()
    application.listen(options.port)
    tornado.autoreload.start()
    io_loop.start()
