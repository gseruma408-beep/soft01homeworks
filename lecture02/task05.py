talent = float(input("Enter talent: \n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))

#conveesion expressions
talent_to_pounds = 20
pounds_to_lots = 32
lots_to_gram = 13.3

#
total_lots = (talent * talent_to_pounds * pounds_to_lots) + (pounds * pounds_to_lots) + lots

total_gram = total_lots * lots_to_gram
print("grams: ", total_gram)

print("kilograms: ", (total_gram/1000))

