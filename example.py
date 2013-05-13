from smartfilter import SmartFilter
from smartfilter import NetworkException
from smartfilter import BadInputParameter, BadAPIKey, RequestTooLarge
from smartfilter import InternalError, AccountQuotaExceeded

key = 'key goes here'
whitelist = 'whitelist goes here'
input = 'the <script>alert("quick brown fox");</script> jumps over the lazy dog'

smartfilter = SmartFilter(key)

try:
  # Verify (returns a boolean)
  print smartfilter.verify()
  # Info (returns a dict with the goodies)
  print smartfilter.info()
  # Detect (returns a dict with the goodies)
  print smartfilter.detect(input, whitelist)
  # Filter (returns a dict with the goodies)
  print smartfilter.filter(input, whitelist)
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
