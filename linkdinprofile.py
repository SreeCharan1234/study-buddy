from linkedin_api import Linkedin
try:
    api = Linkedin("sree9484", "Sree@1234")
    profile = api.get_profile('sree9484')
    print(profile)
except Exception as e:
    print(f"An error occurred: {e}")
