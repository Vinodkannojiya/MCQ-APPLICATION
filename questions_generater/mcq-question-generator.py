from datetime import datetime
import random
# -*- coding:utf-8 -*-

def multiplication_table():
    subject_name = "MATH_TABLES_"
    nums = range(1, 31)
    multiplier =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    current_date = datetime.now().strftime("%Y-%m-%d")
    ans_list = []
    for num in nums:
        for mul in multiplier:
            ans = num * mul
            ans_list.append(ans)
            opt1 = ans
            opt2 = ans - 1
            opt3 = ans + 1
            opt4 = ans + 2
            opts = [opt1, opt2, opt3, opt4]
            options = random.sample(opts, len(opts))

            question_query = f"insert into `learning`.`question_table` " \
            f"(subject_name,question_number,question,option1,option2,option3,option4,answer,added_date) values " \
            f"('{subject_name}{num}',{mul},'{num} X {mul}',{options[0]},{options[1]},{options[2]},{options[3]},{ans},'{current_date}');"
            print(question_query)
        answer_query = f"insert into `learning`.`answer_table` " \
                       f"(subject_name, ans1, ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,added_date) values " \
                       f"('{subject_name}{num}',{ans_list[0]},{ans_list[1]},{ans_list[2]},{ans_list[3]},{ans_list[4]},{ans_list[5]}," \
                       f"{ans_list[6]},{ans_list[7]},{ans_list[8]},{ans_list[9]},'{current_date}');"
        print(answer_query)
        ans_list.clear()

def word_generate():
    subject_name = "ENGLISH_WORDS_"
    current_date = datetime.now().strftime("%Y-%m-%d")
    ans_list = []
    words_in_hindi = ["प्रसन्न", "आनंदपूर्ण", "अति प्रसन्न", "चप्पल", "मन बहलाना", "आनंदमय", "हंसमुख", "प्रसन्न",
                      "भारी भरकम", "बहुत बड़ा", "विशालकाय", "बड़ा", "बहुत छोटा", "प्रचंड", "पतली-दुबली", "नन्हा, कमजोर",
                      "उधार लेना", "उधार देना / कर्ज़ देना", "दान करना", "योगदान देना", "सम्पति", "सम्राट", "वैभव",
                      "महिमा", "भ्रष्टाचार", "लोक-तंत्र / जनतंत्र", "गुलाम", "विद्रोह", "आन्दोलन", "दूल्हा", "सिंदूर",
                      "विवाह", "परंपरा", "समारोह", "गिला", "नरम", "मसालेदार", "तेलमय", "खट्टा", "ऊंचाई", "लम्बाई",
                      "चौराई", "जुलूस, बारात, जलूस", "विदाई", "कड़वा", "मीठा", "गहराई", "कोमलता", "कठोरता",
                      "धूर्त व्यक्ति", "निकम्मा", "बेहूदा", "सनकी", "स्वादिष्ट", "मजबूती", "मोटाई", "पापी", "हरामी",
                      "कमीना", "चोरी", "डकैती", "सेंधमारी", "तस्करी", "धोखा", "अपराध", "छत", "चौक", "गोबर", "धागा",
                      "गड्ढा", "आनंदित", "बेवकूफ", "हत्या", "चारपाई, खटिया", "कीचड़", "बहिष्कार करना", "संविधान",
                      "गणतंत्र", "अधिकार", "दुल्हन", "मैं", "उसके", "सुबह", "शाम", "सरल", "कठिन", "कई", "स्वर", "हर",
                      "की ओर", "युद्ध", "रखना", "जैसा", "आदमी", "वर्ष", "आया", "शो", "के खिलाफ", "के लिए", "पर", "हैं",
                      "साथ", "वे", "कि", "वह", "था", "यात्रा", "कम", "हो", "पर", "इस", "से", "द्वारा", "गरम", "शब्द",
                      "लेकिन", "क्या", "कुछ", "कर सकते हैं", "बाहर", "अन्य", "थे", "जो", "कर", "उनके", "समय", "अगर",
                      "होगा", "कैसे", "कहा", "एक", "प्रत्येक", "बता", "करता है", "सेट", "तीन", "चाहते हैं", "हवा",
                      "अच्छी तरह से", "भी", "खेलने", "छोटे", "अंत", "डाल", "घर", "पढ़ा", "हाथ", "बंदरगाह", "बड़ा",
                      "जादू", "जोड़", "और भी", "भूमि", "यहाँ", "चाहिए", "बड़ा", "उच्च", "ऐसा", "का पालन करें",
                      "अधिनियम", "क्यों", "पूछना", "पुरुषों", "परिवर्तन", "चला गया", "प्रकाश", "तरह", "बंद", "आवश्यकता",
                      "घर", "तस्वीर", "कोशिश", "हमें", "फिर", "पशु", "बिंदु", "मां", "दुनिया", "निकट", "बनाना", "आत्म",
                      "पृथ्वी", "पिता", "किसी भी", "नई", "काम", "हिस्सा", "लेना", "प्राप्त", "जगह", "निर्मित", "जीना",
                      "जहां", "के बाद", "वापस", "थोड़ा", "केवल", "दौर", "अच्छा", "मुझे", "दे", "हमारे", "नीचे", "नाम",
                      "बहुत", "के माध्यम से", "बस", "फार्म", "वाक्य", "महान", "लगता है", "कहना", "मदद", "कम", "रेखा",
                      "अलग", "बारी", "कारण", "ज्यादा", "मतलब", "पहले", "चाल", "सही", "लड़का", "पुराना", "भी", "वही",
                      "वह", "सब", "वहाँ", "जब", "ऊपर", "उपयोग", "अपने", "रास्ता", "के बारे में", "कई", "तो", "उन्हें",
                      "लिखना", "होगा", "जैसा", "तो", "इन", "उसके", "लंबे समय तक", "कर", "बात", "देखना", "उसे", "दो",
                      "है", "देखो", "अधिक", "दिन", "सकता है", "जाना", "आ", "किया", "संख्या", "ध्वनि", "नहीं", "सबसे",
                      "लोग", "मेरे", "अधिक", "पता", "पानी", "से", "कॉल", "पहले", "कौन", "मई", "नीचे", "पक्ष", "गया",
                      "अब", "लगता है", "सिर", "खड़े", "खुद", "पेज", "चाहिए", "देश", "पाया", "जवाब", "स्कूल", "बढ़ने",
                      "अध्ययन", "अब तक", "सीखना", "संयंत्र", "कवर", "भोजन", "सूरज", "चार", "के बीच", "राज्य", "रखना",
                      "आंख", "कभी नहीं", "पिछले", "चलो", "सोचा", "शहर", "पेड़", "पार", "खेत", "शुरुआत", "हो सकता है",
                      "कहानी", "देखा", "दूर", "समुद्र", "आकर्षित", "छोड़ा", "देर से", "चलाने", "ऐसा नहीं", "जबकि",
                      "प्रेस", "करीब", "रात", "असली", "जीवन", "कुछ", "उत्तर", "किताब", "ले", "ले लिया", "विज्ञान",
                      "खाने", "कमरे", "दोस्त", "शुरू हुआ", "विचार", "मछली", "पहाड़", "रोक", "एक बार", "आधार", "सुनना",
                      "घोड़ा", "कटौती", "यकीन", "घड़ी", "रंग", "चेहरा", "लकड़ी", "मुख्य", "खुला", "प्रतीत", "एक साथ",
                      "अगला", "सफेद", "बच्चों", "प्रारंभ करना", "मिला", "चलना", "उदाहरण", "आसानी", "कागज", "समूह",
                      "सदैव", "संगीत", "उन", "दोनों", "मार्क", "अक्सर", "पत्र", "जब तक", "मील", "नदी", "कार", "पैर",
                      "देखभाल", "दूसरा", "पर्याप्त", "सादे", "लड़की", "हमेशा की तरह", "युवा", "तैयार", "ऊपर", "कभी",
                      "लाल", "सूची", "हालांकि", "लग रहा है", "वार्ता", "पक्षी", "शीघ्र", "शरीर", "कुत्ते", "परिवार",
                      "प्रत्यक्ष", "ढोंग", "छोड़", "गीत", "नाप", "दरवाजा", "उत्पाद", "काला", "कम", "अंक", "क्लास",
                      "हवा", "सवाल", "होना", "पूरा", "जहाज", "क्षेत्र", "आधा", "रॉक", "आदेश", "आग", "दक्षिण", "समस्या",
                      "टुकड़ा", "बताया", "पता था", "पास", "के बाद से", "शीर्ष", "पूरे", "राजा", "सड़क", "इंच", "गुणा",
                      "कुछ नहीं", "कोर्स", "रहना", "पहिया", "पूर्ण", "बल", "नीला", "वस्तु", "तय", "सतह", "गहरा", "चांद",
                      "द्वीप", "पैर", "प्रणाली", "व्यस्त", "परीक्षण", "रिकॉर्ड", "नाव", "आम", "सोना", "संभव", "विमान",
                      "जगह", "सूखा", "आश्चर्य", "हंसी", "हजार", "पहले", "भागा", "जाँच", "खेल", "आकार", "समानता", "गरम",
                      "मिस", "लाया", "गर्मी", "बर्फ", "टायर", "लाना", "हां", "दूर", "भरने", "पूर्व", "रंग", "भाषा",
                      "के बीच", "इकाई", "बिजली", "शहर", "ठीक", "कुछ", "मक्खी", "गिरावट", "नेतृत्व", "रोना", "अंधेरा",
                      "मशीन", "नोट", "इंतजार", "योजना", "आंकड़ा", "सितारा", "बॉक्स", "संज्ञा", "क्षेत्र", "बाकी", "सही",
                      "सक्षम", "पाउंड", "किया", "सुंदरता", "ड्राइव", "खड़ा हुआ", "होते हैं", "सामने", "सिखाना",
                      "सप्ताह", "अंतिम", "दिया", "हरे रंग", "ओह", "त्वरित", "विकसित", "सागर", "गर्म", "मुक्त", "मिनट",
                      "मजबूत", "विशेष", "मन", "पीछे", "स्पष्ट", "पूंछ", "उत्पादन", "तथ्य", "अंतरिक्ष", "सुना",
                      "सर्वश्रेष्ठ", "घंटे", "बेहतर", "सच", "दौरान", "सौ", "पांच", "याद", "कदम", "शीघ्र", "पकड़",
                      "पश्चिम", "जमीन", "ब्याज", "तक पहुँचने", "तेजी", "क्रिया", "गाना", "सुनो", "छह", "तालिका",
                      "पैटर्न", "धीमी", "केंद्र", "प्यार", "व्यक्ति", "धन", "सेवा कर", "प्रकट", "सड़क", "नक्शा",
                      "बारिश", "नियम", "शासन", "खींच", "ठंड", "नोटिस", "आवाज", "ऊर्जा", "शिकार", "संभावित", "बिस्तर",
                      "भाई", "अंडा", "सवारी", "सेल", "विश्वास है", "शायद", "उठाओ", "अचानक", "गिनती", "वर्ग", "कारण",
                      "लंबाई", "का प्रतिनिधित्व", "कला", "विषय", "क्षेत्र", "आकार", "भिन्न हो", "बसा", "बोलना", "वजन",
                      "सामान्य", "बर्फ", "मामला", "वृत्त", "जोड़ी", "शामिल", "विभाजन", "शब्दांश", "लगा", "भव्य", "गेंद",
                      "अभी तक", "लहर", "ड्रॉप", "दिल", "AM", "वर्तमान", "भारी", "नृत्य", "इंजन", "स्थिति", "बांह",
                      "विस्तृत", "स्टील अथॉरिटी ऑफ इंडिया", "सामग्री", "अंश", "वन", "बैठना", "दौड़", "खिड़की", "दुकान",
                      "गर्मियों", "सफर", "नींद", "साबित", "लोन", "पैर", "व्यायाम", "दीवार", "पकड़", "माउंट", "इच्छा",
                      "आसमान", "बोर्ड", "हर्ष", "सर्दियों", "शनि", "लिखित", "जंगली", "साधन", "रखा", "कांच", "घास",
                      "गाय", "काम", "बढ़त", "साइन", "यात्रा", "अतीत", "मुलायम", "मज़ा", "उज्ज्वल", "गैस", "मौसम", "माह",
                      "लाख", "भालू", "खत्म", "खुश", "आशा", "फूल", "कपड़े", "अजीब", "चला गया", "व्यापार", "राग",
                      "यात्रा", "कार्यालय", "प्राप्त करना", "पंक्ति", "मुंह", "सटीक", "प्रतीक", "मरना", "कम से कम",
                      "मुसीबत", "चिल्लाओ", "सिवाय", "लिखा", "बीज", "स्वर", "शामिल होने", "सुझाव है", "साफ", "तोड़",
                      "महिला", "यार्ड", "वृद्धि", "बुरा", "झटका", "तेल", "खून", "स्पर्श", "बढ़ी", "प्रतिशत", "मिश्रण",
                      "टीम", "तार", "लागत", "खोया", "ब्राउन", "पहनना", "बगीचा", "बराबर", "भेजा", "चयन", "गिर गया",
                      "फिट", "प्रवाह", "मेला", "बैंक", "इकट्ठा", "बचा", "नियंत्रण", "दशमलव", "कान", "बाकी", "काफी",
                      "तोड़ दिया", "मामले", "बीच", "हत्या", "बेटा", "झील", "पल", "पैमाने", "जोर", "वसंत", "निरीक्षण",
                      "बच्चे", "सीधे", "व्यंजन", "राष्ट्र", "शब्दकोश", "दूध", "गति", "विधि", "अंग", "भुगतान", "उम्र",
                      "अनुभाग", "पोशाक", "बादल", "आश्चर्य", "शांत", "पत्थर", "छोटे", "चढ़ाई", "शीतल", "डिजाइन", "गरीब",
                      "बहुत", "प्रयोग", "तल", "कुंजी", "लोहा", "एकल", "छड़ी", "फ्लैट", "बीस", "त्वचा", "मुस्कान",
                      "क्रीज", "छेद", "कूद", "बच्चे", "आठ", "गांव", "मिलो", "जड़", "खरीद", "उठाना", "हल", "धातु",
                      "चाहे", "धक्का", "सात", "पैरा", "तीसरे", "करेगा", "आयोजित", "बाल", "वर्णन", "कुक", "मंजिल", "भी",
                      "परिणाम", "जला", "पहाड़ी", "सुरक्षित", "बिल्ली", "सदी", "विचार करना", "प्रकार", "कानून", "बिट",
                      "तट", "नकल", "वाक्यांश", "चुप", "लंबा", "रेत", "मिट्टी", "रोल", "तापमान", "उंगली", "उद्योग",
                      "मूल्य", "लड़ाई", "झूठ", "हरा", "उत्तेजित", "प्राकृतिक", "देखें", "भावना", "राजधानी", "नहीं होगा",
                      "कुर्सी", "खतरे", "फल", "अमीर", "मोटी", "सैनिक", "प्रक्रिया", "संचालित", "अभ्यास", "अलग",
                      "मुश्किल", "चिकित्सक", "कृपया", "रक्षा", "दोपहर", "फसल", "आधुनिक", "तत्व", "मारना", "छात्र",
                      "कोने", "पार्टी", "आपूर्ति", "जिसका", "स्थिति जानें", "अंगूठी", "चरित्र", "कीट", "पकड़ा", "अवधि",
                      "संकेत मिलता है", "रेडियो", "बात", "एटम", "मानव", "इतिहास", "प्रभाव", "बिजली", "उम्मीद", "हड्डी",
                      "रेल", "कल्पना", "प्रदान", "सहमत", "इस प्रकार", "कोमल", "महिला", "कप्तान", "अनुमान", "आवश्यक",
                      "तेज़", "पंख", "प्रसिद्ध", "डॉलर", "धारा", "डर", "दृष्टि", "पतली", "त्रिकोण", "ग्रह", "जल्दी करो",
                      "प्रमुख", "कॉलोनी", "घड़ी", "मेरा", "टाई", "दर्ज", "प्रमुख", "ताजा", "खोज", "भेजें", "पीले",
                      "बंदूक", "की अनुमति", "प्रिंट", "मृत", "हाजिर", "रेगिस्तान", "सूट", "वर्तमान", "लिफ्ट", "गुलाब",
                      "पहुंचना", "मास्टर", "ट्रैक", "माता – पिता", "किनारे", "विभाजन", "चादर", "पदार्थ", "एहसान",
                      "कनेक्ट", "पोस्ट", "पिता", "रोटी", "चार्ज", "उचित", "चलना", "अधिसूचना", "काटा", "बार", "प्रस्ताव",
                      "खंड", "गुलाम", "बतख", "पल", "बाजार", "डिग्री", "आबाद", "लड़की", "प्रिय", "दुश्मन", "उत्तर",
                      "पेय", "संदेश", "सब्ज़ी", "घटित", "समर्थन", "भाषण", "प्रकृति", "सीमा", "भाप", "प्रस्ताव", "पथ",
                      "तरल", "लॉग इन करें", "मतलब", "भागफल", "दांत", "खोल", "गर्दन", "ऑक्सीजन", "चीनी", "मौत", "सुंदर",
                      "कौशल", "महिलाओं", "मौसम", "समाधान", "चुंबक", "चांदी", "धन्यवाद", "शाखा", "मैच", "प्रत्यय",
                      "भारी", "बहन", "स्टील", "चर्चा", "आगे", "इसी तरह", "गाइड", "अनुभव", "स्कोर", "सेब", "खरीदा",
                      "नेतृत्व", "पिच", "कोट", "सामूहिक", "कार्ड", "बैंड", "रस्सी", "मटका", "पर्ची", "जीत", "मंजूरी",
                      "सपना", "शर्त", "फ़ीड", "उपकरण", "संपूर्ण", "बुनियादी", "गंध", "घाटी", "और न ही", "डबल", "सीट",
                      "जारी रखने के", "खंड", "चार्ट", "घटाना"]
    words_in_english = ["GLAD", "JOYFUL", "ECSTATIC", "SLIPPERS", "AMUSED", "BLISSFUL", "CHEERFUL", "DELIGHTED",
                        "GIGANTIC", "IMMENSE", "MAMMOTH", "MASSIVE", "TINY", "COLOSSAL", "PETITE", "PUNY",
                        "BORROW", "LEND", "DONATE", "CONTRIBUTE", "ASSETS", "EMPEROR", "SPLENDOR", "MAJESTY",
                        "CORRUPTION", "DEMOCRACY", "SLAVERY", "REBELLION", "PROTEST", "GROOM", "VERMILION",
                        "MATRIMONY", "TRADITION", "CEREMONY", "MOIST", "BLAND", "SPICY", "GREASY", "SOUR",
                        "HEIGHT", "LENGTH", "WIDTH", "PROCESSION", "FAREWELL", "BITTER", "SWEET", "DEPTH",
                        "SOFTNESS", "HARDNESS", "RASCAL", "USELESS", "GAGA", "FREAK", "DELICIOUS", "STRENGTH",
                        "THICKNESS", "SINNER", "BASTARD", "SLAVISH", "THEFT", "ROBBERY", "BURGLARY",
                        "SMUGGLING", "FRAUD", "CRIME", "ROOF", "PLAZA", "DUNG", "THREAD", "PIT", "MERRY",
                        "STUPID", "MURDER", "DOSS", "MUD", "BOYCOTT", "CONSTITUTION", "REPUBLIC", "POSSESSION",
                        "BRIDE", "I", "HIS", "MORNING", "EVENING", "SIMPLE", "HARD", "SEVERAL", "VOWEL", "EVERY",
                        "TOWARD", "WAR", "LAY", "AS", "MAN", "YEAR", "CAME", "SHOW", "AGAINST", "FOR", "ON", "ARE",
                        "WITH", "THEY", "THAT", "HE", "WAS", "TRAVEL", "LESS", "BE", "AT", "THIS", "FROM", "BY", "HOT",
                        "WORD", "BUT", "WHAT", "SOME", "CAN", "OUT", "OTHER", "WERE", "WHICH", "DO", "THEIR", "TIME",
                        "IF", "WILL", "HOW", "SAID", "AN", "EACH", "TELL", "DOES", "SET", "THREE", "WANT", "AIR",
                        "WELL", "ALSO", "PLAY", "SMALL", "END", "PUT", "HOME", "READ", "HAND", "PORT", "LARGE", "SPELL",
                        "ADD", "EVEN", "LAND", "HERE", "MUST", "BIG", "HIGH", "SUCH", "FOLLOW", "ACT", "WHY", "ASK",
                        "MEN", "CHANGE", "WENT", "LIGHT", "KIND", "OFF", "NEED", "HOUSE", "PICTURE", "TRY", "US",
                        "AGAIN", "ANIMAL", "POINT", "MOTHER", "WORLD", "NEAR", "BUILD", "SELF", "EARTH", "FATHER",
                        "ANY", "NEW", "WORK", "PART", "TAKE", "GET", "PLACE", "MADE", "LIVE", "WHERE", "AFTER", "BACK",
                        "LITTLE", "ONLY", "ROUND", "GOOD", "ME", "GIVE", "OUR", "UNDER", "NAME", "VERY", "THROUGH",
                        "JUST", "FORM", "SENTENCE", "GREAT", "THINK", "SAY", "HELP", "LOW", "LINE", "DIFFER", "TURN",
                        "CAUSE", "MUCH", "MEAN", "BEFORE", "MOVE", "RIGHT", "BOY", "OLD", "TOO", "SAME", "SHE", "ALL",
                        "THERE", "WHEN", "UP", "USE", "YOUR", "WAY", "ABOUT", "MANY", "THEN", "THEM", "WRITE", "WOULD",
                        "LIKE", "SO", "THESE", "HER", "LONG", "MAKE", "THING", "SEE", "HIM", "TWO", "HAS", "LOOK",
                        "MORE", "DAY", "COULD", "GO", "COME", "DID", "NUMBER", "SOUND", "NO", "MOST", "PEOPLE", "MY",
                        "OVER", "KNOW", "WATER", "THAN", "CALL", "FIRST", "WHO", "MAY", "DOWN", "SIDE", "BEEN", "NOW",
                        "FIND", "HEAD", "STAND", "OWN", "PAGE", "SHOULD", "COUNTRY", "FOUND", "ANSWER", "SCHOOL",
                        "GROW", "STUDY", "STILL", "LEARN", "PLANT", "COVER", "FOOD", "SUN", "FOUR", "BETWEEN", "STATE",
                        "KEEP", "EYE", "NEVER", "LAST", "LET", "THOUGHT", "CITY", "TREE", "CROSS", "FARM", "START",
                        "MIGHT", "STORY", "SAW", "FAR", "SEA", "DRAW", "LEFT", "LATE", "RUN", "DON’T", "WHILE", "PRESS",
                        "CLOSE", "NIGHT", "REAL", "LIFE", "FEW", "NORTH", "BOOK", "CARRY", "TOOK", "SCIENCE", "EAT",
                        "ROOM", "FRIEND", "BEGAN", "IDEA", "FISH", "MOUNTAIN", "STOP", "ONCE", "BASE", "HEAR", "HORSE",
                        "CUT", "SURE", "WATCH", "COLOR", "FACE", "WOOD", "MAIN", "OPEN", "SEEM", "TOGETHER", "NEXT",
                        "WHITE", "CHILDREN", "BEGIN", "GOT", "WALK", "EXAMPLE", "EASE", "PAPER", "GROUP", "ALWAYS",
                        "MUSIC", "THOSE", "BOTH", "MARK", "OFTEN", "LETTER", "UNTIL", "MILE", "RIVER", "CAR", "FEET",
                        "CARE", "SECOND", "ENOUGH", "PLAIN", "GIRL", "USUAL", "YOUNG", "READY", "ABOVE", "EVER", "RED",
                        "LIST", "THOUGH", "FEEL", "TALK", "BIRD", "SOON", "BODY", "DOG", "FAMILY", "DIRECT", "POSE",
                        "LEAVE", "SONG", "MEASURE", "DOOR", "PRODUCT", "BLACK", "SHORT", "NUMERAL", "CLASS", "WIND",
                        "QUESTION", "HAPPEN", "COMPLETE", "SHIP", "AREA", "HALF", "ROCK", "ORDER", "FIRE", "SOUTH",
                        "PROBLEM", "PIECE", "TOLD", "KNEW", "PASS", "SINCE", "TOP", "WHOLE", "KING", "STREET", "INCH",
                        "MULTIPLY", "NOTHING", "COURSE", "STAY", "WHEEL", "FULL", "FORCE", "BLUE", "OBJECT", "DECIDE",
                        "SURFACE", "DEEP", "MOON", "ISLAND", "FOOT", "SYSTEM", "BUSY", "TEST", "RECORD", "BOAT",
                        "COMMON", "GOLD", "POSSIBLE", "PLANE", "STEAD", "DRY", "WONDER", "LAUGH", "THOUSAND", "AGO",
                        "RAN", "CHECK", "GAME", "SHAPE", "EQUATE", "HOT", "MISS", "BROUGHT", "HEAT", "SNOW", "TIRE",
                        "BRING", "YES", "DISTANT", "FILL", "EAST", "PAINT", "LANGUAGE", "AMONG", "UNIT", "POWER",
                        "TOWN", "FINE", "CERTAIN", "FLY", "FALL", "LEAD", "CRY", "DARK", "MACHINE", "NOTE", "WAIT",
                        "PLAN", "FIGURE", "STAR", "BOX", "NOUN", "FIELD", "REST", "CORRECT", "ABLE", "POUND", "DONE",
                        "BEAUTY", "DRIVE", "STOOD", "CONTAIN", "FRONT", "TEACH", "WEEK", "FINAL", "GAVE", "GREEN", "OH",
                        "QUICK", "DEVELOP", "OCEAN", "WARM", "FREE", "MINUTE", "STRONG", "SPECIAL", "MIND", "BEHIND",
                        "CLEAR", "TAIL", "PRODUCE", "FACT", "SPACE", "HEARD", "BEST", "HOUR", "BETTER", "TRUE",
                        "DURING", "HUNDRED", "FIVE", "REMEMBER", "STEP", "EARLY", "HOLD", "WEST", "GROUND", "INTEREST",
                        "REACH", "FAST", "VERB", "SING", "LISTEN", "SIX", "TABLE", "PATTERN", "SLOW", "CENTER", "LOVE",
                        "PERSON", "MONEY", "SERVE", "APPEAR", "ROAD", "MAP", "RAIN", "RULE", "GOVERN", "PULL", "COLD",
                        "NOTICE", "VOICE", "ENERGY", "HUNT", "PROBABLE", "BED", "BROTHER", "EGG", "RIDE", "CELL",
                        "BELIEVE", "PERHAPS", "PICK", "SUDDEN", "COUNT", "SQUARE", "REASON", "LENGTH", "REPRESENT",
                        "ART", "SUBJECT", "REGION", "SIZE", "VARY", "SETTLE", "SPEAK", "WEIGHT", "GENERAL", "ICE",
                        "MATTER", "CIRCLE", "PAIR", "INCLUDE", "DIVIDE", "SYLLABLE", "FELT", "GRAND", "BALL", "YET",
                        "WAVE", "DROP", "HEART", "AM", "PRESENT", "HEAVY", "DANCE", "ENGINE", "POSITION", "ARM", "WIDE",
                        "SAIL", "MATERIAL", "FRACTION", "FOREST", "SIT", "RACE", "WINDOW", "STORE", "SUMMER", "TRAIN",
                        "SLEEP", "PROVE", "LONE", "LEG", "EXERCISE", "WALL", "CATCH", "MOUNT", "WISH", "SKY", "BOARD",
                        "JOY", "WINTER", "SAT", "WRITTEN", "WILD", "INSTRUMENT", "KEPT", "GLASS", "GRASS", "COW", "JOB",
                        "EDGE", "SIGN", "VISIT", "PAST", "SOFT", "FUN", "BRIGHT", "GAS", "WEATHER", "MONTH", "MILLION",
                        "BEAR", "FINISH", "HAPPY", "HOPE", "FLOWER", "CLOTHE", "STRANGE", "GONE", "TRADE", "MELODY",
                        "TRIP", "OFFICE", "RECEIVE", "ROW", "MOUTH", "EXACT", "SYMBOL", "DIE", "LEAST", "TROUBLE",
                        "SHOUT", "EXCEPT", "WROTE", "SEED", "TONE", "JOIN", "SUGGEST", "CLEAN", "BREAK", "LADY", "YARD",
                        "RISE", "BAD", "BLOW", "OIL", "BLOOD", "TOUCH", "GREW", "CENT", "MIX", "TEAM", "WIRE", "COST",
                        "LOST", "BROWN", "WEAR", "GARDEN", "EQUAL", "SENT", "CHOOSE", "FELL", "FIT", "FLOW", "FAIR",
                        "BANK", "COLLECT", "SAVE", "CONTROL", "DECIMAL", "EAR", "ELSE", "QUITE", "BROKE", "CASE",
                        "MIDDLE", "KILL", "SON", "LAKE", "MOMENT", "SCALE", "LOUD", "SPRING", "OBSERVE", "CHILD",
                        "STRAIGHT", "CONSONANT", "NATION", "DICTIONARY", "MILK", "SPEED", "METHOD", "ORGAN", "PAY",
                        "AGE", "SECTION", "DRESS", "CLOUD", "SURPRISE", "QUIET", "STONE", "TINY", "CLIMB", "COOL",
                        "DESIGN", "POOR", "LOT", "EXPERIMENT", "BOTTOM", "KEY", "IRON", "SINGLE", "STICK", "FLAT",
                        "TWENTY", "SKIN", "SMILE", "CREASE", "HOLE", "JUMP", "BABY", "EIGHT", "VILLAGE", "MEET", "ROOT",
                        "BUY", "RAISE", "SOLVE", "METAL", "WHETHER", "PUSH", "SEVEN", "PARAGRAPH", "THIRD", "SHALL",
                        "HELD", "HAIR", "DESCRIBE", "COOK", "FLOOR", "EITHER", "RESULT", "BURN", "HILL", "SAFE", "CAT",
                        "CENTURY", "CONSIDER", "TYPE", "LAW", "BIT", "COAST", "COPY", "PHRASE", "SILENT", "TALL",
                        "SAND", "SOIL", "ROLL", "TEMPERATURE", "FINGER", "INDUSTRY", "VALUE", "FIGHT", "LIE", "BEAT",
                        "EXCITE", "NATURAL", "VIEW", "SENSE", "CAPITAL", "WON’T", "CHAIR", "DANGER", "FRUIT", "RICH",
                        "THICK", "SOLDIER", "PROCESS", "OPERATE", "PRACTICE", "SEPARATE", "DIFFICULT", "DOCTOR",
                        "PLEASE", "PROTECT", "NOON", "CROP", "MODERN", "ELEMENT", "HIT", "STUDENT", "CORNER", "PARTY",
                        "SUPPLY", "WHOSE", "LOCATE", "RING", "CHARACTER", "INSECT", "CAUGHT", "PERIOD", "INDICATE",
                        "RADIO", "SPOKE", "ATOM", "HUMAN", "HISTORY", "EFFECT", "ELECTRIC", "EXPECT", "BONE", "RAIL",
                        "IMAGINE", "PROVIDE", "AGREE", "THUS", "GENTLE", "WOMAN", "CAPTAIN", "GUESS", "NECESSARY",
                        "SHARP", "WING", "FAMOUS", "DOLLAR", "STREAM", "FEAR", "SIGHT", "THIN", "TRIANGLE", "PLANET",
                        "HURRY", "CHIEF", "COLONY", "CLOCK", "MINE", "TIE", "ENTER", "MAJOR", "FRESH", "SEARCH", "SEND",
                        "YELLOW", "GUN", "ALLOW", "PRINT", "DEAD", "SPOT", "DESERT", "SUIT", "CURRENT", "LIFT", "ROSE",
                        "ARRIVE", "MASTER", "TRACK", "PARENT", "SHORE", "DIVISION", "SHEET", "SUBSTANCE", "FAVOR",
                        "CONNECT", "POST", "DAD", "BREAD", "CHARGE", "PROPER", "WALK      ", "NOTIFICATION", "FORK",
                        "BAR", "OFFER", "SEGMENT", "SLAVE", "DUCK", "INSTANT", "MARKET", "DEGREE", "POPULATE", "CHICK",
                        "DEAR", "ENEMY", "REPLY", "DRINK", "MESSAGE", "VEGETABLES", "OCCUR", "SUPPORT", "SPEECH",
                        "NATURE", "RANGE", "STEAM", "MOTION", "PATH", "LIQUID", "LOG", "MEANT", "QUOTIENT", "TEETH",
                        "SHELL", "NECK", "OXYGEN", "SUGAR", "DEATH", "PRETTY", "SKILL", "WOMEN", "SEASON", "SOLUTION",
                        "MAGNET", "SILVER", "THANK", "BRANCH", "MATCH", "SUFFIX", "HUGE", "SISTER", "STEEL", "DISCUSS",
                        "FORWARD", "SIMILAR", "GUIDE", "EXPERIENCE", "SCORE", "APPLE", "BOUGHT", "LED", "PITCH", "COAT",
                        "MASS", "CARD", "BAND", "ROPE", "POT", "SLIP", "WIN", "SANCTION", "DREAM",
                        "CONDITION", "FEED", "TOOL", "TOTAL", "BASIC", "SMELL", "VALLEY", "NOR", "DOUBLE", "SEAT",
                        "CONTINUE", "BLOCK", "CHART", "SUBTRACT"]



    for i in range(len(words_in_hindi)):
    # for i in range(20):
        options_val = random.sample(words_in_english, len(words_in_english))
        diffrent_options = set([options_val[0], options_val[1], options_val[2]])
        while len(diffrent_options) != 3:
            options = random.sample(words_in_english, len(words_in_english))
            diffrent_options = set(options[0], options[1], options[2])
        diffrent_options_list = list(diffrent_options)
        diffrent_options_list.append(words_in_english[i])
        options = random.sample(diffrent_options_list, len(diffrent_options_list))

        ans_list.append(words_in_english[i])
        question_query = f"insert into `learning`.`question_table` " \
            f"(subject_name,question_number,question,option1,option2,option3,option4,answer,added_date) values " \
            f"('{subject_name}{(i//10)+1}',{(i % 10) + 1},'{words_in_hindi[i]}','{options[0]}','{options[1]}'," \
                         f"'{options[2]}','{options[3]}','{words_in_english[i]}','{current_date}');"
        print(question_query)
        diffrent_options_list.remove(words_in_english[i])
        if (i % 10) + 1 == 10:
            answer_query = f"insert into `learning`.`answer_table` " \
                           f"(subject_name, ans1, ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10,added_date) values " \
                           f"('{subject_name}{(i//10)+1}','{ans_list[0]}','{ans_list[1]}','{ans_list[2]}','{ans_list[3]}','{ans_list[4]}','{ans_list[5]}','" \
                           f"{ans_list[6]}','{ans_list[7]}','{ans_list[8]}','{ans_list[9]}','{current_date}');"
            print(answer_query)
            ans_list.clear()

if __name__ == "__main__":
    # multiplication_table()
    word_generate()