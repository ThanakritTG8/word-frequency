import csv
import ast
from collections import Counter


def count_frequency(filename, place_name):
    output_data = []
    universal_pos_tags = ["ADJ","ADP","ADV","AUX",
        "CCONJ","DET","INTJ","NOUN","NUM",
        "PART","PRON","PROPN","PUNCT",
        "SCONJ","SYM","VERB","X"]
    max_lenght = 0
    with open('./data/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        all_words = []
        for row in csv_reader:
            line_count += 1
            # print(line_count)

            matrixAr = []

            mystring = row[place_name]
            mystring = mystring.replace(' (', '(')
            #mystring = mystring.replace(",('<s/>', 'PUNCT')", '')
            #mystring = mystring.replace(",('.', 'PUNCT')", '')
            #mystring = mystring.replace(",('.', 'PUNCT')", '')

            #mystring = mystring.replace(')', ' ')
            mystring = mystring.replace("', '", ' - ')
            mystring = mystring.replace("'", '')

            # to remove head [[ and tail ]]
            b = mystring.replace("[[", "").replace("]]", "")
            for line in b.split('], ['):
                row_ = list(line.split(','))
                matrixAr.append(row_)
            # print(matrixAr)
            unique_words = []
            for sentence in matrixAr:
                for word in sentence:
                    unique_words.append(word)

            # find unique words in any comments
            #unique_words = unique(sentence)
            all_words.extend(unique_words)

        bf = dict(Counter(all_words))  # counting words

        af = {k: bf[k]
              for k in sorted(bf, key=bf.get, reverse=True)}  # sort asending
        print(f"Was found {len(af)} unique words. ")
        #sort
        #ADJ: adjective
        #ADP: adposition
        #ADV: adverb
        #AUX: auxiliary
        #CCONJ: coordinating conjunction
        #DET: determiner
        #INTJ: interjection
        #NOUN: noun
        #NUM: numeral
        #PART: particle
        #PRON: pronoun
        #PROPN: proper noun
        #PUNCT: punctuation
        #SCONJ: subordinating conjunction
        #SYM: symbol
        #VERB: verb
        #X: other


        for pos_tag in universal_pos_tags:
            result = []
            for element in af:
                if element.find(pos_tag) != -1 :
                    count = af.get(element, '')
                    result.append({"word": element, "count": count})
            output_data.append({"tag":pos_tag,"data":result})
        
        for tag_with_count in output_data :
            print(f'tag {tag_with_count["tag"]} count {len(tag_with_count["data"])}')
            count = len(tag_with_count["data"])
            if max_lenght <=  count :
                max_lenght = count

        #i = 1
        #for element in af:
            #count = af.get(element, '')
            ##print(f"{i}.{element} : {count}")
            #output_data.append({"word": element, "count": count})
            ## if(count==1):
            ##    break
            #i += 1

        print(
            f'Read file:{filename} place:{place_name} lines:{line_count} lines.')
    # print(output_data)
    with open('./output/'+filename+place_name+'.csv', mode='w', newline='', encoding='utf-8') as writefile:
        fieldnames = ["ADJ","ADJ_COUNT","ADP","ADP_COUNT","ADV","ADV_COUNT","AUX","AUX_COUNT",
        "CCONJ","CCONJ_COUNT","DET","DET_COUNT","INTJ","INTJ_COUNT","NOUN","NOUN_COUNT","NUM","NUM_COUNT",
        "PART","PART_COUNT","PRON","PRON_COUNT","PROPN","PROPN_COUNT","PUNCT","PUNCT_COUNT",
        "SCONJ","SCONJ_COUNT","SYM","SYM_COUNT","VERB","VERB_COUNT","X","X_COUNT"]
            
            
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)
        writer.writeheader()
        
        i = 0
        
        while(i<max_lenght) :
            adj_word = " "
            adj_count = " "
            adp_word = " "
            adp_count = " "
            adv_word = " "
            adv_count = " "
            aux_word = " "
            aux_count = " "
            cconj_word = " "
            cconj_count = " "
            det_word = " "
            det_count = " "
            intj_word = " "
            intj_count = " "
            noun_word = " "
            noun_count = " "
            num_word = " "
            num_count = " "
            part_word = " "
            part_count = " "
            pron_word = " "
            pron_count = " "
            propn_word = " "
            propn_count = " "
            punct_word = " "
            punct_count = " "
            sconj_word = " "
            sconj_count = " "
            sym_word = " "
            sym_count = " "
            verb_word = " "
            verb_count = " "
            x_word = " "
            x_count = " "
            
            if i < len(output_data[0]["data"]) : 
                adj_word = output_data[0]["data"][i]["word"]
                adj_count = output_data[0]["data"][i]["count"]
            if i < len(output_data[1]["data"]) : 
                adp_word = output_data[1]["data"][i]["word"]
                adp_count = output_data[1]["data"][i]["count"]
            if i < len(output_data[2]["data"]) : 
                adv_word = output_data[2]["data"][i]["word"]
                adv_count = output_data[2]["data"][i]["count"]
            if i < len(output_data[3]["data"]) : 
                aux_word = output_data[3]["data"][i]["word"]
                aux_count = output_data[3]["data"][i]["count"]
            if i < len(output_data[4]["data"]) : 
                cconj_word = output_data[4]["data"][i]["word"]
                cconj_count = output_data[4]["data"][i]["count"]
            if i < len(output_data[5]["data"]) : 
                det_word = output_data[5]["data"][i]["word"]
                det_count = output_data[5]["data"][i]["count"]
            if i < len(output_data[6]["data"]) : 
                intj_word = output_data[6]["data"][i]["word"]
                intj_count = output_data[6]["data"][i]["count"]
            if i < len(output_data[7]["data"]) : 
                noun_word = output_data[7]["data"][i]["word"]
                noun_count = output_data[7]["data"][i]["count"]
            if i < len(output_data[8]["data"]) : 
                num_word = output_data[8]["data"][i]["word"]
                num_count = output_data[8]["data"][i]["count"]
            if i < len(output_data[9]["data"]) : 
                part_word = output_data[9]["data"][i]["word"]
                part_count = output_data[9]["data"][i]["count"]
            if i < len(output_data[10]["data"]) : 
                pron_word = output_data[10]["data"][i]["word"]
                pron_count = output_data[10]["data"][i]["count"]
            if i < len(output_data[11]["data"]) : 
                propn_word = output_data[11]["data"][i]["word"]
                propn_count = output_data[11]["data"][i]["count"]
            if i < len(output_data[12]["data"]) : 
                punct_word = output_data[12]["data"][i]["word"]
                punct_count = output_data[12]["data"][i]["count"]
            if i < len(output_data[13]["data"]) : 
                sconj_word = output_data[13]["data"][i]["word"]
                sconj_count = output_data[13]["data"][i]["count"]
            if i < len(output_data[14]["data"]) : 
                sym_word = output_data[14]["data"][i]["word"]
                sym_count = output_data[14]["data"][i]["count"]
            if i < len(output_data[15]["data"]) : 
                verb_word = output_data[15]["data"][i]["word"]
                verb_count = output_data[15]["data"][i]["count"]
            if i < len(output_data[16]["data"]) : 
                x_word = output_data[16]["data"][i]["word"]
                x_count = output_data[16]["data"][i]["count"]   

            writer.writerow({"ADJ":adj_word,"ADJ_COUNT":adj_count,"ADP":adp_word,"ADP_COUNT":adp_count,
                "ADV":adv_word,"ADV_COUNT":adv_count,"AUX":aux_word,"AUX_COUNT":aux_count,
                "CCONJ":cconj_word,"CCONJ_COUNT":cconj_count,"DET":det_word,"DET_COUNT":det_count,
                "INTJ":intj_word,"INTJ_COUNT":intj_count,"NOUN":noun_word,"NOUN_COUNT":noun_count,
                "NUM":num_word,"NUM_COUNT":num_count,"PART":part_word,"PART_COUNT":part_count,
                "PRON":pron_word,"PRON_COUNT":pron_count,"PROPN":propn_word,"PROPN_COUNT":propn_count,
                "PUNCT":punct_word,"PUNCT_COUNT":punct_count,"SCONJ":sconj_word,"SCONJ_COUNT":sconj_count,
                "SYM":sym_word,"SYM_COUNT":sym_count,"VERB":verb_word,"VERB_COUNT":verb_count,
                "X":x_word,"X_COUNT":x_count})

            i += 1


        #i = 0
        #for row in output_data:
            
        #    word = output_data[i]["word"]
        #    count = output_data[i]["count"]
            
            
        #    writer.writerow(
        #        {'word': word, 'count': count})
        #    i += 1
        #print(
        #    f' Wrote file:{filename} place:{place_name} lines:{i} lines.')


def count_frequency_tltk():
    filename = "aftertpyewords - deepcutVsTltk"
    output_data = []
    with open('./data/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        all_words = []
        line_count = 0
        for row in csv_reader:
            line_count += 1
            mystring = row["tltk"]
            matrixAr = []

            mystring = mystring.replace(' (', '(')
            mystring = mystring.replace(",('<s/>', 'PUNCT')", '')
            mystring = mystring.replace(",('.', 'PUNCT')", '')
            mystring = mystring.replace(",('.', 'PUNCT')", '')

            #mystring = mystring.replace(')', ' ')
            mystring = mystring.replace("', '", ' - ')
            mystring = mystring.replace("'", '')

            # to remove head [[ and tail ]]
            b = mystring.replace("[[", "").replace("]]", "")
            for line in b.split('], ['):
                row_ = list(line.split(','))
                matrixAr.append(row_)
            #print(matrixAr)
            unique_words = []
            for sentence in matrixAr:
                for word in sentence:
                    unique_words.append(word)
                 # find unique words in any comments
            #unique_words = unique(unique_words)
            all_words.extend(unique_words)
           

        bf = dict(Counter(all_words))  # counting words

        af = {k: bf[k]
              for k in sorted(bf, key=bf.get, reverse=True)}  # sort asending
        print(f"Was found {len(af)} unique words. ")
        i = 1
        for element in af:
            count = af.get(element, '')
            #print(f"{i}.{element} : {count}")
            output_data.append({"word": element, "count": count})
            # if(count==1):
            #    break
            i += 1

        print(f'Read file:{filename} lines:{line_count} lines.')
    with open('./output/'+filename+'_tltk.csv', mode='w', newline='', encoding='utf-8') as writefile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        for row in output_data:
            word = output_data[i]["word"]
            count = output_data[i]["count"]
            writer.writerow(
                {'word': word, 'count': count})
            i += 1
        print(
    f' Wrote file:{filename} lines:{line_count} lines.')


def count_frequency_deepcut():
    filename = "aftertpyewords - deepcutVsTltk"
    output_data = []
    with open('./data/'+filename+'.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        all_words = []
        line_count = 0
        for row in csv_reader:
            line_count += 1
            mystring = row["deepcut"]
            mystring = ast.literal_eval(mystring)
            #print(mystring)
            mystring = unique(mystring)
            all_words.extend(mystring)


        bf = dict(Counter(all_words))  # counting words

        af = {k: bf[k]for k in sorted(bf, key=bf.get, reverse=True)}  # sort asending
        print(f"Was found {len(af)} unique words. ")
        i = 1
        for element in af:
            count = af.get(element, '')
            #print(f"{i}.{element} : {count}")
            output_data.append({"word": element, "count": count})
            # if(count==1):
            #    break
            i += 1

        print(f'Read file:{filename} lines:{line_count} lines.')
    
    with open('./output/'+filename+'_deepcut.csv', mode='w', newline='', encoding='utf-8') as writefile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(writefile, fieldnames=fieldnames)
        writer.writeheader()
        i = 0
        for row in output_data:
            word = output_data[i]["word"]
            count = output_data[i]["count"]
            writer.writerow(
                {'word': word, 'count': count})
            i += 1
        print(
            f' Wrote file:{filename} lines:{line_count} lines.')



def unique(sentence):

    # insert the list to the set
    list_set = set(sentence)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list


files_name = ["aftertpyeword - google", "aftertpyeword - tripadvisor"]
places = ["patong", "promthep", "wat"]

for file_name in files_name :
    for place in places :
        count_frequency(file_name , place)


#count_frequency_deepcut()
#count_frequency_tltk()
