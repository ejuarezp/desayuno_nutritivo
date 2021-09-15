from music21 import note, stream, duration

N1 = note.Note('C')
N2 = note.Note('C')
N2.offset = 1
N3 = note.Note('G')
N3.offset = 2
N4 = note.Note('G')
N4.offset = 3
N5 = note.Note('A')
N5.offset = 4
N6 = note.Note('A')
N6.offset = 5
N7 = note.Note('G')
N7.offset = 6
N7.duration = duration.Duration('half')

Secuencia1 = [N1, N2, N3, N4, N5, N6, N7]
st = stream.Stream(Secuencia1)

st.write('midi', fp="martinillo.mid")

