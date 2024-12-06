import pandas as pd
import time
from datetime import datetime

def convert_to_epoch(date_str, time_str, date_format):
    """Converts date and time strings to epoch time."""
    dt = datetime.strptime(f"{date_str} {time_str}", date_format)
    return int(time.mktime(dt.timetuple()))

def filter_rows(file_path, start_epoch, end_epoch):
    """Filters rows based on epoch time range."""
    df = pd.read_excel(file_path)
    return df[(df['timeFirst'] >= start_epoch) & (df['timeFirst'] <= end_epoch)]

def main():
    datasets = [
        {
            "timestamps": [
                ("Thursday, July 6, 2017", "14:19", "14:21"),
                ("Thursday, July 6, 2017", "14:33", "14:35"),
                ("Thursday, July 6, 2017", "14:53", "15:00"),
                ("Thursday, July 6, 2017", "15:04", "15:45")
            ],
            "date_format": "%A, %B %d, %Y %H:%M",
            "file_path": "C:\\Users\\kinid\\OneDrive\\Desktop\\UNB\\2017\\flow_extracted\\2017_Infiltration_Flow\\Thursday_Infiltration_Flow_flows.xlsx",
            "output_file": "C:\\Users\\kinid\\OneDrive\\Desktop\\Thursday_Infiltration_Flow_filtered.xlsx"
        },
        {
            "timestamps": [
                ("Thursday-01-03-2018", "9:57", "10:55"),
                ("Thursday-01-03-2018", "14:00", "15:37"),
                ("Thursday-01-03-2018", "14:00", "15:37")
            ],
            "date_format": "%A-%d-%m-%Y %H:%M",
            "file_path": "../flow_extracted/infiltration_p3/infiltration_p3_flows.xlsx",
            "output_file": "infiltration_p3.xlsx"
        }
    ]

    for dataset in datasets:
        filtered_data = pd.DataFrame()
        for date, start_time, end_time in dataset["timestamps"]:
            start_epoch = convert_to_epoch(date, start_time, dataset["date_format"])
            end_epoch = convert_to_epoch(date, end_time, dataset["date_format"])
            filtered_rows = filter_rows(dataset["file_path"], start_epoch, end_epoch)
            filtered_data = pd.concat([filtered_data, filtered_rows])

        filtered_data = filtered_data.drop_duplicates()
        filtered_data.to_excel(dataset["output_file"], index=False)

if __name__ == "__main__":
    main()
