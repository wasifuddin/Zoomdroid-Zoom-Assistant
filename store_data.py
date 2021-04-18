import pandas as pd




def add_meeting(newrow):
    print(newrow)
    df = pd.read_csv('meet_details.csv')
    # df = df.append(newrow, ignore_index= True)
    df.loc[len(df.index)] = newrow
    df = df.sort_values(by='Timing', ascending=True)
    df['Meet_day'] = pd.Categorical(df['Meet_day'], ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat"])
    df = df.sort_values('Meet_day')
    df.to_csv('meet_details.csv', index = False)

def signup_entry(newlogin):
    print(newlogin)
    df1 = pd.read_csv('user_data.csv')
    df1 = df1.append(newlogin, ignore_index=True)
    df1.to_csv('user_data.csv', index=False)


