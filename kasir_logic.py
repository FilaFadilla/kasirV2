prices = {
    'ayam_betutu': 139000,
    'gurame_terbang': 139000,
    'lalapan_mentah': 15000,
    'pete_goreng': 19000,
    'plecing_kangkung': 35000,
    'sambal_dadak': 15000
}


def hitung_total(qty):
    total = 0
    detail = {}

    for key, price in prices.items():
        jumlah = qty.get(key, 0) or 0
        if jumlah > 0:
            subtotal = price * jumlah
            detail[key] = subtotal
            total += subtotal

    return total, detail


def hitung_diskon(total, ultah_flag):
    if (ultah_flag or '').lower() == 'y':
        return int(total * 0.3)
    return 0
