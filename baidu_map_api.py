import requests

class baidu_map_api(object):

    def __init__(self):
        self.api_key = "***"
        self.print_every_records = 500

    def getLatLong(self, address_lst):
        '''
        Get the latitude and longtitude with address.
        :param lst: list[str]
        :return: list of LAT/LONG, address fail list.
        '''
        result = []
        failure = 0
        fail_lst = []
        counter = 0
        for address in address_lst:
            try:
                url = f"http://api.map.baidu.com/geocoder?output=json&key={self.api_key}&address=" + str(address)
                response = requests.get(url)
                answer = response.json()
                if answer['status'] == "OK":
                    result.append(str(answer['result']['location']['lat']) + "," + str(answer['result']['location']['lng']))
                else:
                    failure += 1
                    result.append('n.a.')
            except Exception as e:
                failure += 1
                fail_lst.append(address)
                result.append('n.a.')
                continue

            counter += 1
            if counter % self.print_every_records == 0:
                print('Finished', counter, 'address.')

        print('Address found:', len(address_lst) - failure)
        print('Fail:', failure)
        return result, fail_lst

    def getDistrict(self, lat_long_lst):
        '''
        Get the location to district level with LAT/LONG variables.
        :param lat_long_lst: [latitude, longitude]
        :return: list of cities, list of district, lat/long fail list.
        '''

        result_city = []
        result_district = []
        fail_lst = []
        failure = 0
        counter = 0
        for lat_long in lat_long_lst:
            try:
                url = f"http://api.map.baidu.com/geocoder?output=json&key={self.api_key}&location=" + str(lat_long)
                response = requests.get(url)
                answer = response.json()
                if answer['status'] == "OK":
                    city = answer['result']['addressComponent']['city']
                    district = answer['result']['addressComponent']['district']
                    result_city.append(city)
                    result_district.append(district)
                else:
                    failure += 1
                    fail_lst.append(lat_long)
                    result_city.append("n.a.")
                    result_district.append("n.a.")
            except Exception as e:
                failure += 1
                fail_lst.append(lat_long)
                result_city.append("n.a.")
                result_district.append("n.a.")
                continue

            counter += 1
            if counter % self.print_every_records == 0:
                print('Finished', counter, 'latitude and longitude.')

        print('Address found:', len(lat_long_lst) - failure)
        print('Fail:', failure)

        return result_city, result_district, fail_lst

if __name__ == '__main__':
    print("BAIDU MAP API.")