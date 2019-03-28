from src import paas_data

DEFAULT_RESPONSE = "Not sure what you mean. Try *'do'* "
SAY_HELLO = "Hello World!"
FP_CREDS = "*CREDENTIALS*: \n *url*: {} \n".format(paas_data.PLATFORM_1['url']) + \
           "*user*: {} \n".format(paas_data.PLATFORM_1['user']) + \
           "*password*: {}\n".format(paas_data.PLATFORM_1['password'])

HZ_CREDS = "*CREDENTIALS*: \n *url*: {} \n".format(paas_data.PLATFORM_2['url']) + \
          "*user*: {} \n".format(paas_data.PLATFORM_2['user']) + \
          "*password*: {}\n".format(paas_data.PLATFORM_2['password'])
