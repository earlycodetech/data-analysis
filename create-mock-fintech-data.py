gender = ['male','female']
states_str = 'Borno Taraba Kaduna Bauchi Yobe Zamfara Adamawa Kwara Kebbi Benue Plateau Kogi Oyo Nasarawa Sokoto Katsina Jigawa CrossRiver Kano Gombe Edo Delta Ogun Ondo Rivers Bayelsa Osun FCT Enugu AkwaIbom Ekiti Abia Ebonyi Imo Anambra Lagos'
states = states_str.split()
geodem = ['rural','urban']

data_states = []
data_gender = []
data_geodem = []

data_age = list(np.random.randint(18,80,10000))
data_amount = list(np.random.randint(500,1000000,10000))

current = 1
from random import randrange

while current < 10001:
    data_states.append(states[randrange(0,36)])
    data_gender.append(gender[randrange(0,2)])
    data_geodem.append(geodem[randrange(0,2)])
    
    current += 1
data2 = {
    'State':data_states,'Gender':data_gender,
    'Geography':data_geodem,'Age':data_age,'Deposit':data_amount
}

fintech = pd.DataFrame(data2)
