from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

class Expanded_SPAAN_Model:
    
    def __init__(self):

        # model 1
        aa_freq = Input(shape=(20))
        dense_1 = Dense(30, activation='sigmoid')(aa_freq)
        dense_1_2 = Dense(1, activation='sigmoid')(dense_1)
        
        # model 2.1
        multiplet_freq_1 = Input(shape=(20))
        dense_2_1_1 = Dense(28, activation='sigmoid')(multiplet_freq_1)
        dense_2_1_2 = Dense(1, activation='sigmoid')(dense_2_1_1)
        # model 2.2
        multiplet_freq_2 = Input(shape=(20))
        dense_2_2_1 = Dense(28, activation='sigmoid')(multiplet_freq_2)
        dense_2_2_2 = Dense(1, activation='sigmoid')(dense_2_2_1)
        # model 2.3
        multiplet_freq_3 = Input(shape=(20))
        dense_2_3_1 = Dense(28, activation='sigmoid')(multiplet_freq_3)
        dense_2_3_2 = Dense(1, activation='sigmoid')(dense_2_3_1)
        # concatenate outputs
        concat_1 = Concatenate()([dense_2_1_2, dense_2_2_2, dense_2_3_2])
        dense_2_4 = Dense(1, activation='sigmoid')(concat_1)
        
        # model 3
        dipept_freq = Input(shape=(400))
        dense_3 = Dense(500, activation='sigmoid')(dipept_freq)
        dense_3_2 = Dense(1, activation='sigmoid')(dense_3)
        
        # model 4
        charge_comp = Input(shape=(26))
        dense_4 = Dense(40, activation='sigmoid')(charge_comp)
        dense_4_2 = Dense(1, activation='sigmoid')(dense_4)
        
        # model 5
        hydrophob_comp = Input(shape=(50))
        dense_5 = Dense(40, activation='sigmoid')(hydrophob_comp)
        dense_5_2 = Dense(1, activation='sigmoid')(dense_5)
        
        # final concatenation
        concat_2 = Concatenate()([dense_1_2, dense_2_4, dense_3_2, dense_4_2, dense_5_2])
        final_dense = Dense(1, activation='sigmoid')(concat_2)
        
        model = Model(inputs=[[aa_freq, multiplet_freq_1, multiplet_freq_2, multiplet_freq_3, dipept_freq, charge_comp, hydrophob_comp], y], outputs=final_dense)
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics='accuracy')
        
        self.model = model
        
    def get_model(self):
        return self.model