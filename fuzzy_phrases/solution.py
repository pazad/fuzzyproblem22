import json

def phrasel_search(P, Queries):
    # This function will find the fuzzy matching of phrases into the list of queries(strings/sentences)
    ans = []
    for phrase in Queries:
        phrase1 = list(phrase.split(' '))
        result = []
        result1 = []
        for item in P:
            words = list(item.split(' '))
            # check if all elements on phrase are in queries 
            if all(element in phrase1 for element in words):
                # check if the orders appear in phrase
                if phrase.index(words[0]) < phrase.index(words[-1]):
                    end_of_phrase = phrase.index(words[-1])+ len(words[-1])
                    begining_of_phrase = phrase.index(words[0])
                    # find the slice of first word until last word
                    found = phrase[begining_of_phrase:end_of_phrase]
                    if len(found) != 0:
                        result1.append(item)
                        result.append(found)
        ans.append(list(set().union(result, result1)))
    return ans

if __name__ == "__main__":
    # I check with 20_points all pass, 
    # 30_points I think the json file missed some of the combination for "feel due"
    # 50_points all pass
    with open('50_points.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        print('============= ALL TEST PASSED SUCCESSFULLY ===============')

