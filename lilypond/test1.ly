\version "2.14.2"
\score{
	\new Staff <<
		\tempo 4 = 90
		\new Voice \chordmode {
			\set midiInstrument = #"acoustic grand"
			c2
			f
			g:7
			c
		}
	>>
	\midi{
		\context {
			\Voice
			\consists "Staff_performer"
		}
	}
}
