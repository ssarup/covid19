class Location(object):
    def __init__(self):
        self._country = None
        self._state = None
        self._county = None
        self._city = None

    def country(self, country_):
        self._country = country_
        return self

    def state(self, state_):
        self._state = state_
        return self

    def county(self, county_):
        self._county = county_
        return self

    def city(self, city_):
        self._city = city_
        return self

    def __str__(self):
        retVal = ['[']
        if self._country is not None:
            retVal.append('country = {0}'.format(self._country))
        if self._state is not None:
            retVal.append('state = {0}'.format(self._state))
        if self._county is not None:
            retVal.append('county = {0}'.format(self._county))
        if self._city is not None:
            retVal.append('city = {0}'.format(self._city))
        retVal.append(']')
        return ' ,'.join(retVal)
