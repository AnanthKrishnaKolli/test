import random

features=[]
n=10
for i in range(n):
	features.append(random.randint(1,20))
print(features)


def normalized_features(features):
    mean = sum(features)/ len(features)
    variance = sum( (x-mean)**2 for x in features ) / len(features)
    std_dev = variance**0.5
    normalized_features = [ (x-mean)/std_dev for x in features ]
    return normalized_features

print(normalized_features(features))