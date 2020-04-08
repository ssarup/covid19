class Location(object):
    def __init__(self, country_ = None, state_ = None, county_ = None, city_ = None):
        self._country = country_
        self._state = state_
        self._county = county_
        self._city = city_

    @property
    def country(self):
        return self._country

    @property
    def state(self):
        return self._state

    @property
    def county(self):
        return self._county

    @property
    def city(self):
        return self._city

    @country.setter
    def country(self, country_):
        return Location(country_, self._state, self._county, self._city)

    @state.setter
    def state(self, state_):
        return Location(self._country, state_, self._county, self._city)

    @county.setter
    def county(self, county_):
        return Location(self._country, self._state, county_, self._city)

    @city.setter
    def city(self, city_):
        return Location(self._country, self._state, self._county, city_)

    def __eq__(self, other_):
        if isinstance(other_, Location):
            return self._country == other_._country and \
                   self._state == other_._state and \
                   self._county == other_._county and \
                   self._city == other_._city

    def __hash__(self):
        return hash(str(self))

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
