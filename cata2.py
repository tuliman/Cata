def duplicate_count(text):
    text=list(i.lower() for i in text)
    
    text = ([i for i in text  if text.count(i)>1])


    return int(len(list(set(text))))


print(duplicate_count("indivisibility"))
