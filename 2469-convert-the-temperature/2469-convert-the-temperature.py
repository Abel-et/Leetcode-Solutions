class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        # kelvin = c + 273.15
        # Fahrenheit = c+32)9/7
        kelvin = celsius + 273.15
        fahrenheit = celsius*1.80 + 32 
        return [kelvin,fahrenheit]
        