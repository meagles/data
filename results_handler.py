import pandas as pd

def read_results_csv(results_csv_path):
    results_df = pd.read_csv(results_csv_path)
#     results_df.set_index("election_date", inplace=True)
    return results_df

def read_turnout_csv(turnout_csv_path):
    turnout_df = pd.read_csv(turnout_csv_path)
    return turnout_df

def narrow_to_election(results_df, election_date):
    elec_df = results_df[results_df['election_date'] == election_date]
    return elec_df

def narrow_to_contest(results_df, contest_name):
    contest_df = results_df[results_df['contest_name'] == contest_name]
    return contest_df

def narrow_to_candidate(results_df, candidate_selection):
    candidate_df = results_df[results_df['candidate_selection'] == candidate_selection]
    return candidate_df

def narrow_to_ward(results_df, ward_num):
    ward_df = results_df[results_df['ward'] == ward_num]
    return ward_df

def get_elections(results_df):
    return results_df.election_date.unique()

def get_contests(results_df):
    return results_df.contest_name.unique()

def get_candidates(results_df):
    return results_df.candidate_selection.unique()

sum_precinct_aggregation_function = {'vote_count': 'sum'}
groupby_columns = ['election_date', 'contest_name', 'candidate_selection', 'ward', 'precinct']
def sum_votes_by_precinct(results_df):
    summed_df = results_df.groupby(groupby_columns, as_index=False).aggregate(sum_precinct_aggregation_function)
    return summed_df

sum_precinct_turnout_aggregation_function = {'vote_count': 'sum', 'reg_voters':'first'}
turnout_groupby_columns = ['election_date', 'ward', 'precinct']
def sum_turnout_by_precinct(turnout_df):
    summed_df = turnout_df.groupby(turnout_groupby_columns, as_index=False).aggregate(sum_precinct_turnout_aggregation_function)
    summed_df['turnout_percent'] = 100 * summed_df['vote_count'] / summed_df['reg_voters']
    return summed_df


