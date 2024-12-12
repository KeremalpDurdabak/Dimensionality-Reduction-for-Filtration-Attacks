import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder

# Function to load and preprocess dataset
def load_and_preprocess(file_path, type_label, included_columns=None):
    df = pd.read_excel(file_path)
    df['type'] = type_label
    if included_columns:
        df = df[included_columns]
    return df

# Function to combine, shuffle, and reset index of datasets
def combine_shuffle_datasets(dfs):
    combined_df = pd.concat(dfs)
    shuffled_df = shuffle(combined_df, random_state=42).reset_index(drop=True)
    return shuffled_df

# Function to label encode excluding 'type' column
def label_encode(df):
    le = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        if column != 'type':
            df[column] = le.fit_transform(df[column])
    return df

# File paths and type labels
datasets = [
    {"file_path": "Lorem/Ipsum/Benign_Flows.xlsx", "type_label": 0},
    {"file_path": "Lorem/Ipsum/Infiltration_Flows_1.xlsx", "type_label": 1},
    {"file_path": "Lorem/Ipsum/Infiltration_Flows_2.xlsx", "type_label": 1},
    {"file_path": "Lorem/Ipsum/Infiltration_Flows_3.xlsx", "type_label": 1}
]

# Included columns
included_columns = [
    "duration", "numHdrs", "hdrDesc", "ethType", "l4Proto", "numPktsSnt", "numPktsRcvd",
    "numBytesSnt", "numBytesRcvd", "minPktSz", "maxPktSz", "avePktSize",
    "stdPktSize", "maxIAT", "aveIAT", "stdIAT", "pktps", "bytps",
    "pktAsm", "bytAsm", "tcpFStat", "ipMindIPID", "ipMaxdIPID", "ipMinTTL",
    "ipMaxTTL", "ipTTLChg", "ipToS", "ipFlags", "ipOptCnt", "ipOptCpCl_Num",
    "ip6OptCntHH_D", "ip6OptHH_D", "tcpISeqN", "tcpPSeqCnt", "tcpSeqSntBytes",
    "tcpSeqFaultCnt", "tcpPAckCnt", "tcpFlwLssAckRcvdBytes", "tcpAckFaultCnt",
    "tcpBFlgtMx", "tcpInitWinSz", "tcpAveWinSz", "tcpMinWinSz", "tcpMaxWinSz",
    "tcpWinSzDwnCnt", "tcpWinSzUpCnt", "tcpWinSzChgDirCnt", "tcpWinSzThRt",
    "tcpFlags", "tcpAnomaly", "tcpOptPktCnt", "tcpOptCnt", "tcpOptions",
    "tcpMSS", "tcpWS", "tcpTmS", "tcpTmER", "tcpEcI", "tcpUtm", "tcpBtm",
    "tcpSSASAATrip", "tcpRTTAckTripMin", "tcpRTTAckTripMax", "tcpRTTAckTripAve",
    "tcpRTTAckTripJitAve", "tcpRTTSseqAA", "tcpRTTAckJitAve",
    "tcpStatesAFlags", "icmpStat", "icmpTCcnt", "icmpBFTypH_TypL_Code",
    "icmpEchoSuccRatio", "icmpPFindex", "connF", "connG",
    "connNumPCnt", "connNumBCnt", "type"
]

# Load, preprocess, and combine datasets
processed_datasets = [
    load_and_preprocess(dataset["file_path"], dataset["type_label"], included_columns)
    for dataset in datasets
]

combined_df = combine_shuffle_datasets(processed_datasets)

# Label encode
combined_df_encoded = label_encode(combined_df)

# Save the final dataset
output_path = "Lorem/Ipsum/combined_processed.xlsx"
combined_df_encoded.to_excel(output_path, index=False)
