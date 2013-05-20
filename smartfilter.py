import requests

class NetworkException(Exception): pass
class BadInputParameter(Exception): pass
class BadAPIKey(Exception): pass
class RequestTooLarge(Exception): pass
class InternalError(Exception): pass
class AccountQuotaExceeded(Exception): pass

class SmartFilter:
  def __init__(self, key):
    self.key = key
    self.base = 'https://api.prevoty.com/1'

  # Endpoint: /key/verify
  def verify(self):
    try:
      options = {'api_key':self.key}
      response = requests.get(self.base + '/key/verify', params=options)
      if response.status_code == 200: 
        return True
      elif response.status_code == 400: 
        raise BadInputParameter()
      elif response.status_code == 403:
        raise BadAPIKey()
      elif response.status_code == 500:
        raise InternalError()
    except requests.exceptions.RequestException:
      raise NetworkException()
    return False

  # Endpoint: /key/info
  def info(self):
    try:
      options = {'api_key':self.key}
      response = requests.get(self.base + '/key/info', params=options)
      if response.status_code == 200: 
        return response.json()
      elif response.status_code == 400: 
        raise BadInputParameter()
      elif response.status_code == 403:
        raise BadAPIKey()
      elif response.status_code == 500:
        raise InternalError()
    except requests.exceptions.RequestException:
      raise NetworkException()
    return {}

  # Endpoint: /rule/verify
  def verify_rule(self, rule_key):
    try:
      options = {'api_key':self.key, 'rule_key':rule_key}
      response = requests.get(self.base + '/rule/verify', params=options)
      if response.status_code == 200: 
        return True
      elif response.status_code == 400: 
        raise BadInputParameter()
      elif response.status_code == 403:
        raise BadAPIKey()
      elif response.status_code == 500:
        raise InternalError()
    except requests.exceptions.RequestException:
      raise NetworkException()
    return False

  # Endpoint: /xss/filter
  def filter(self, input, rule_key):
    try:
      options = {'api_key':self.key, 'input':input, 'rule_key':rule_key}
      response = requests.post(self.base + '/xss/filter', params=options)
      if response.status_code == 200: 
        return response.json()
      elif response.status_code == 400: 
        raise BadInputParameter()
      elif response.status_code == 403:
        raise BadAPIKey()
      elif response.status_code == 413:
        raise RequestTooLarge()
      elif response.status_code == 500:
        raise InternalError()
      elif response.status_code == 507:
        raise AccountQuotaExceeded()
    except requests.exceptions.RequestException:
      raise NetworkException()
    return {}
