# importing the data from the json file

import json 
import difflib
data = json.load(open("data.json"));


def translate(word):
	# Check for the word whether it exists in the dictionary or not
	
	
	if word in data:
		return data[word];
	# if not then return the message that entry is not in data dictionary, we find the
	# the closest match in a list and return the first element of the list as it has 
	#high chance of mapping
	# elif word == closest_match.lower():
	# 	return translate(closest_match);
	elif word.title() in data: # Check for similar words that might start with capital letter or so.
		return data[word.title()];
	elif word.upper() in data:  # Check for acronyms in the code
		return data[word.upper()];
	elif len(difflib.get_close_matches(word,data.keys())) > 0 :
		print("This word does'nt exists in dictionary, closest matches could be:")
		print(difflib.get_close_matches(word,data.keys())[0]);
		print("Do u want to search for the suggested word")
		user_input = input(" Y or N :");
		user_input = user_input.lower();
		if user_input in ['yes','y']:
			return data[difflib.get_close_matches(word,data.keys())[0]];
		else:
			return "Your word does'nt exist.Thanks for using suggested dictionary";
	else:
		return "The word desn't exist";

			

word = input("Enter Word: ");

results = translate(word.lower());
if type(results) == list:

	for result in results:
		print(result);
		print("\n");
else:
	print(results);
# flag=0;
# for key in data:
# 	seq = difflib.SequenceMatcher(None,word.lower(),key)
# 	d = seq.ratio()*100;
# 	if(d>flag):
# 		flag = d;
# 		new_word = key;

# print("Closest Matching one is " + new_word);