#Series of strings
hardware = pdSeries(['Hammer', 'Saw', 'Wrench'])

''' 0 Hammer
    1   Saw
    2   Wrench
    dtype: object'''

#calling string methods apply to eaach element
hardware.str.contains('a')

'''0 True
    1   True
    2   False
    dtype: bool'''

hardware_upper = hardware.str.upper()

''' 0   HAMMER
    1   SAW
    2   WRENCH '''