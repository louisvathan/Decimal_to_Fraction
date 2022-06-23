from fractions import Fraction as f
from math import floor

def d2f(num, data, denominator, rounding, middle_condition):
	min_value = 1/denominator/2
	for i, key in enumerate(data):
		if float(key)-num == 0:
			return (data[key][-1], "Done")
		elif float(key)-num > 0:
			next_num = float(key)
			prev_num = next_num - (1/denominator)
			if rounding == "Round to Nearest Fraction":   # Round to the nearest fraction
				if num-prev_num > next_num-num:
					return (data[key][-1], "Done")
				elif num-prev_num < next_num-num:
					return (data[str(prev_num)][-1], "Done")
				else: # num-prev_num == next_num-num
					if middle_condition == "to Next": # next
						return (data[key][-1], "Done")
					else:
						return (data[str(prev_num)][-1], "Done")
			elif rounding == "Round to Next Fraction": # Round to the next fraction.
				return (data[key][-1], "Done")
			elif rounding == "Round to Previous Fraction":
				return (data[str(prev_num)][-1], "Done")
			elif rounding == "No Rounding": # No Rounding
				return (num, f"Number not rounded. Closest fraction with a denominator limit of 64 is {f(num).limit_denominator(64)}")

def decimal_to_fraction(x, denominator, rounding, middle_condition):
	sixtyfourth = {
							"0.0"   : ["0/64", "0/32", "0/16", "0/8", "0/4", "0/2", "0"],
							"0.015625"  : ["1/64"],
							"0.03125"   : ["2/64", "1/32"],
							"0.046875"  : ["3/64"],
							"0.0625": ["4/64", "2/32", "1/16"],
							"0.078125"  : ["5/64"],
							"0.09375"   : ["6/64", "3/32"],
							"0.109375"  : ["7/64"],
							"0.125" : ["8/64", "4/32", "2/16", "1/8"],
							"0.140625"  : ["9/64"],
							"0.15625"   : ["10/64", "5/32"],
							"0.171875"  : ["11/64"],
							"0.1875": ["12/64", "6/32", "3/16"],
							"0.203125"  : ["13/64"],
							"0.21875"   : ["14/64", "7/32"],
							"0.234375"  : ["15/64"],
							"0.25"  : ["16/64", "8/32", "4/16", "2/8", "1/4"],
							"0.265625"  : ["17/64"],
							"0.28125"   : ["18/64", "9/32"],
							"0.296875"  : ["19/64"],
							"0.3125": ["20/64", "10/32", "5/16"],
							"0.328125"  : ["21/64"],
							"0.34375"   : ["22/64", "11/32"],
							"0.359375"  : ["23/64"],
							"0.375" : ["24/64", "12/32", "6/16", "3/8"],
							"0.390625"  : ["25/64"],
							"0.40625"   : ["26/64", "13/32"],
							"0.421875"  : ["27/64"],
							"0.4375": ["28/64", "14/32", "7/16"],
							"0.453125"  : ["29/64"],
							"0.46875"   : ["30/64", "15/32"],
							"0.484375"  : ["31/64"],
							"0.5"   : ["32/64", "16/32", "8/16", "4/8", "2/4", "1/2"],
							"0.515625"  : ["33/64"],
							"0.53125"   : ["34/64", "17/32"],
							"0.546875"  : ["35/64"],
							"0.5625": ["36/64", "18/32", "9/16"],
							"0.578125"  : ["37/64"],
							"0.59375"   : ["38/64", "19/32"],
							"0.609375"  : ["39/64"],
							"0.625" : ["40/64", "20/32", "10/16", "5/8"],
							"0.640625"  : ["41/64"],
							"0.65625"   : ["42/64", "21/32"],
							"0.671875"  : ["43/64"],
							"0.6875": ["44/64", "22/32", "11/16"],
							"0.703125"  : ["45/64"],
							"0.71875"   : ["46/64", "23/32"],
							"0.734375"  : ["47/64"],
							"0.75"  : ["48/64", "24/32", "12/16", "6/8", "3/4"],
							"0.765625"  : ["49/64"],
							"0.78125"   : ["50/64", "25/32"],
							"0.796875"  : ["51/64"],
							"0.8125": ["52/64", "26/32", "13/16"],
							"0.828125"  : ["53/64"],
							"0.84375"   : ["54/64", "27/32"],
							"0.859375"  : ["55/64"],
							"0.875" : ["56/64", "28/32", "14/16", "7/8"],
							"0.890625"  : ["57/64"],
							"0.90625"   : ["58/64", "29/32"],
							"0.921875"  : ["59/64"],
							"0.9375": ["60/64", "30/32", "15/16"],
							"0.953125"  : ["61/64"],
							"0.96875"   : ["62/64", "31/32"],
							"0.984375"  : ["63/64"],
							"1.0"   : ["64/64", "32/32", "16/16", "8/8", "4/4", "2/2", "1"]
			}

	thirtysecond = {}
	sixteenth = {}
	eights = {}
	fourth = {}
	halfs = {}
	ones = {}

	for i in sixtyfourth:
		if len(sixtyfourth[i]) > 1:
			thirtysecond[i] = sixtyfourth[i]
		if len(sixtyfourth[i]) > 2:
			sixteenth[i] = sixtyfourth[i]
		if len(sixtyfourth[i]) > 3:
			eights[i] = sixtyfourth[i]
		if len(sixtyfourth[i]) > 4:
			fourth[i] = sixtyfourth[i]
		if len(sixtyfourth[i]) > 5:
			halfs[i] = sixtyfourth[i]
		if len(sixtyfourth[i]) > 6:
			ones[i] = sixtyfourth[i]

	whole_num, deci_num = floor(x), x-floor(x)

	if denominator == 64:
		frac, status = d2f(deci_num, sixtyfourth, denominator, rounding, middle_condition)
	elif denominator == 32:
		frac, status = d2f(deci_num, thirtysecond, denominator, rounding, middle_condition)
	elif denominator == 16:
		frac, status = d2f(deci_num, sixteenth, denominator, rounding, middle_condition)
	elif denominator == 8:
		frac, status = d2f(deci_num, eights, denominator, rounding, middle_condition)
	elif denominator == 4:
		frac, status = d2f(deci_num, fourth, denominator, rounding, middle_condition)
	elif denominator == 2:
		frac, status = d2f(deci_num, halfs, denominator, rounding, middle_condition)
	elif denominator == 1:
		frac, status = d2f(deci_num, ones, denominator, rounding, middle_condition)

	if frac == "0":
		conv_num = str(whole_num)
	elif frac == "1":
		conv_num = str(whole_num+1)
	else:
		if str(whole_num) == "0":
			conv_num = str(frac)
		else:
			conv_num = str(whole_num) + " " + str(frac)
	
	return conv_num