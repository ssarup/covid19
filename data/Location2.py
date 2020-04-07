class Location2(object)
    def __init__(self, country_, state_, county_, city_):
        self._country = county_
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

    def country(self, country_):
        return Location2(country_, self._state, self._county, self._city)

    def state(self, state_):
        return Location2(self._country, state_, self._county, self._city)

    def county(self, county_):
        return Location2(self._country, self._state, county_, self._city)

    def city(self, city_):
        return Location2(self._country, self._state, self._county, city_)