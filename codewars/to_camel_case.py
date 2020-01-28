def to_camel_case(text):
    return ''.join(text[0] + text.title().translate(None, '_-')[1:] if text else text)
    # if text:
    #     if "_" in text or "-" in text:
    #         if text[0].isupper():
    #             return ''.join(x for x in text.replace("_", ' ').replace("-", ' ').title() if not x.isspace())
    #         else:
    #             return ''.join(x for x in text[0] + 
    #                 text.replace("_", ' ').replace("-", ' ').title()[1:] if not x.isspace())
    #     else:
    #       return ''.join(x for x in text.title() if not x.isspace())
    #  else:
            # return ''


text = "Testing function to_camel_case"
text2 = "Basic tests"
text3 = "The-Stealth-Warrior"
text4 = "the-Stealth-Warrior"
text5 = "A-B-C"
text6 = ""
print to_camel_case(text)
