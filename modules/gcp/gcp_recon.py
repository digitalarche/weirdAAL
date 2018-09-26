'''
This module handles the core GCP recon functionality by asking all the services
that have functions that done have arguments if we can access them :-)
'''



from libs.gcp.gcp_iam import *
#from libs.gcp.gcp_storage import *

credentials = service_account.Credentials.from_service_account_file(
    filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/cloud-platform'])

service = googleapiclient.discovery.build(
    'iam', 'v1', credentials=credentials)

def module_gcp_recon_all():
    '''
    Main gcp_recon_all module - attempt to connect to each of the services to see if we have some privs
    python3 weirdAAL.py -m gcp_recon_all -t demo
    '''
    try:
        print("IAM List Keys check")
        #print(credentials)
        gcp_iam_list_keys(credentials.service_account_email, service)
        #list_service_accounts('best-indian-restaurant-691ad')
    except HttpError as e:
        # print(e)
        if e.resp.status in [403, 500, 503]:
            print("\tIAM access denied for {}".format(credentials.service_account_email))
        else:
            print(e)
    except google.auth.exceptions.RefreshError as f:
        print(f)
        print("Service key is invalid exiting")
        sys.exit()
