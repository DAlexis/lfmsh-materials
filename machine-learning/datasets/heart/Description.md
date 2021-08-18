# Context
This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to
this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).
# Content

Attribute Information:

1. age
2. sex
3. chest pain type (4 values) - тип боли в груди
4. resting blood pressure - артериальное давление в покое
5. serum cholestoral in mg/dl - уровень холестерина
6. fasting blood sugar > 120 mg/dl - сахар в крови натощак
7. resting electrocardiographic results (values 0,1,2) - результаты электрокардиографии в покое
8. maximum heart rate achieved - максимальный пульс
9. exercise induced angina - стенокардия, вызванная физической нагрузкой
10. oldpeak = ST depression induced by exercise relative to rest - Уменьшение ST-интервала, вызванное физической нагрузкой по сравнению с покоем
11. the slope of the peak exercise ST segment - крутость ST-интервала при нагрузке												
12. number of major vessels (0-3) colored by flourosopy - количество крупных сосудов, окрашенных при флюорографии ??
13. thal: 3 = normal; 6 = fixed defect; 7 = reversable defect - Талассеми́я (анемия Кули) — заболевание, наследуемое по рецессивному типу (двухаллельная система), в основе которого лежит снижение синтеза полипептидных цепей, входящих в структуру нормального гемоглобина.  

The names and social security numbers of the patients were recently removed from the database, replaced with dummy values. One file has been "processed", that one containing the Cleveland database. All four unprocessed files also exist in this directory.

To see Test Costs (donated by Peter Turney), please see the folder "Costs"

Acknowledgements
Creators:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D.
Donor:
David W. Aha (aha '@' ics.uci.edu) (714) 856-8779

Inspiration
Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).

See if you can find any other trends in heart data to predict certain cardiovascular events or find any clear indications of heart health.
