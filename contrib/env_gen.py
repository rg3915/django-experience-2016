#!/usr/bin/env python

CONFIG_STRING = """
DEBUG=True
SECRET_KEY=#%u+ztjei)+wdr!cp8haft7jmi=_uk%cv1vp8_r1+2-97uo^5g
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME

#LANGUAGE_CODE=
#TIME_ZONE=

#DEFAULT_FROM_EMAIL=
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
""".strip()

# Writing our configuration file to '.env'
with open('.env', 'w') as configfile:
    configfile.write(CONFIG_STRING)
