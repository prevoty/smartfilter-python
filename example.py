from smartfilter import SmartFilter
from smartfilter import NetworkException
from smartfilter import BadInputParameter, BadAPIKey, RequestTooLarge
from smartfilter import InternalError, AccountQuotaExceeded

api_key = 'api key goes here'
rule_key = 'rule key goes here'
input = 'the <script>alert("quick brown fox");</script> jumps over the lazy dog & mouse'

smartfilter = SmartFilter(api_key)

try:
  # Verify (returns a boolean)
  print smartfilter.verify()
  # Info (returns a dict with the goodies)
  print smartfilter.info()
  # VerifyRule (returns a boolean)
  print smartfilter.verify_rule(rule_key)
  # Filter (returns a dict with the goodies)
  print smartfilter.filter(input, rule_key)
except NetworkException:
  print 'Network connectivity issue'
except BadInputParameter:
  print 'Bad input parameter exception'
except BadAPIKey:
  print 'Bad API key'
except RequestTooLarge:
  print 'Request too large'
except InternalError:
  print 'Internal Prevoty error'
except AccountQuotaExceeded:
  print 'Account quota exceeded'
