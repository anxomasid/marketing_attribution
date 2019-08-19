### Shapley Attribution - Settings ###

""" Modules """
import os

""" Google Cloud - Project """
google_cloud_project_id = 'carrefour-159506'
""" Google Cloud - Credentials """
service_account_credentials_file = os.path.join(os.path.dirname(__file__), 'carrefour-159506-8509e798744f.json')
""" BigQuery - Dataset """
dataset_name = '120566275'
""" BigQuery - Table """
table_name = 'ga_sessions'