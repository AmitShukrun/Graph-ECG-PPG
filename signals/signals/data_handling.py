
def data_extraction(data):  # Extracting the data from the Json and separating them into ecg and ppg
    ecg, ppg = [], []

    for key, value in data.items():
        if "ECG" in key:
            ecg.append(value)
        else:
            ppg.append(value)

    return ecg, ppg
