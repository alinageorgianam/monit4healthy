import datetime

CNP_JUDETE = {
    "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor", "06": "Bistrița-Năsăud",
    "07": "Botoșani", "08": "Brașov", "09": "Brăila", "10": "Buzău", "11": "Caraș-Severin", "12": "Cluj",
    "13": "Constanța", "14": "Covasna", "15": "Dâmbovița", "16": "Dolj", "17": "Galați", "18": "Gorj",
    "19": "Harghita", "20": "Hunedoara", "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș",
    "25": "Mehedinți", "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
    "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș", "36": "Tulcea",
    "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "București", "41": "București - Sector 1",
    "42": "București - Sector 2", "43": "București - Sector 3", "44": "București - Sector 4",
    "45": "București - Sector 5",
    "46": "București - Sector 6", "51": "Călărași", "52": "Giurgiu"
}

def extract_cnp_info(cnp):
    cnp=str(cnp)
    if len(cnp) != 13 or not cnp.isdigit():
        raise ValueError("CNP-ul trebuie sa aiba 13 cifre.")

    # Sex și perioadă
    gender_code = int(cnp[0])
    if gender_code in [1, 3, 5, 7]:
        gender = "Masculin"
    elif gender_code in [2, 4, 6, 8]:
        gender = "Feminin"

    if gender_code in [1, 2]:  # 1900-1999
        birth_century = 1900
    elif gender_code in [3, 4]:  # 1800-1899
        birth_century = 1800
    elif gender_code in [5, 6]:  # 2000-2099
        birth_century = 2000
    else:
        birth_century = None

    an = int(cnp[1:3])
    if birth_century:
        an += birth_century
    luna = int(cnp[3:5])
    zi = int(cnp[5:7])

    try:
        zi_nastere = datetime.date(an, luna, zi)
    except ValueError:
        raise ValueError("Date invalide in CNP.")

    cod_judet = cnp[7:9]
    judet = CNP_JUDETE.get(cod_judet, "Necunoscut")

    nr_unic = int(cnp[9:12])
    cifra_control = int(cnp[12])

    today = datetime.date.today()
    varsta = today.year - zi_nastere.year - ((today.month, today.day) < (zi_nastere.month, zi_nastere.day))

    cnp_info = {
        "gender": gender,
        "zi_nastere": zi_nastere,
        "varsta": varsta,
        "judet": judet,
        "nr_unic": nr_unic,
        "cifra_control": cifra_control
    }

    return cnp_info


