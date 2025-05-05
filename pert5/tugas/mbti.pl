% --------------------------
% DATABASE
% --------------------------
:- dynamic sifat_pos/1.
:- dynamic sifat_neg/1.

% Daftar kepribadian
kepribadian("Singa").
kepribadian("Lumba-lumba").
kepribadian("Burung Hantu").
kepribadian("Semut").
kepribadian("Kura-kura").

% Relasi sifat dengan kepribadian
sifat(nyaman_keramaian, "Singa").
sifat(suka_merencanakan, "Singa").
sifat(hal_baru, "Singa").
sifat(tak_sesuai_rencana, "Singa").
sifat(bosan, "Singa").

sifat(nyaman_keramaian, "Lumba-lumba").
sifat(cemas, "Lumba-lumba").
sifat(hal_baru, "Lumba-lumba").
sifat(paham_perasaan, "Lumba-lumba").
sifat(bosan, "Lumba-lumba").
sifat(hindari_konflik, "Lumba-lumba").

sifat(suka_merencanakan, "Burung Hantu").
sifat(cemas, "Burung Hantu").
sifat(paham_perasaan, "Burung Hantu").
sifat(sendiri, "Burung Hantu").
sifat(tak_sesuai_rencana, "Burung Hantu").
sifat(hindari_konflik, "Burung Hantu").
sifat(sulit_percaya_orang, "Burung Hantu").

sifat(suka_merencanakan, "Semut").
sifat(sendiri, "Semut").
sifat(tak_sesuai_rencana, "Semut").
sifat(sulit_percaya_orang, "Semut").

sifat(suka_merencanakan, "Kura-kura").
sifat(cemas, "Kura-kura").
sifat(paham_perasaan, "Kura-kura").
sifat(sendiri, "Kura-kura").
sifat(tak_sesuai_rencana, "Kura-kura").
sifat(hindari_konflik, "Kura-kura").
sifat(sulit_percaya_orang, "Kura-kura").

% Pertanyaan untuk setiap sifat
pertanyaan(nyaman_keramaian, "Apakah kamu merasa nyaman di keramaian atau bertemu orang baru?").
pertanyaan(suka_merencanakan, "Apakah kamu suka merencanakan sesuatu jauh-jauh hari?").
pertanyaan(cemas, "Apakah kamu cenderung merasa cemas atau khawatir tanpa ada alasan yang jelas?").
pertanyaan(hal_baru, "Apakah kamu senang mencoba hal-hal baru yang belum pernah kamu lakukan sebelumnya?").
pertanyaan(paham_perasaan, "Apakah kamu mudah memahami perasaan orang lain tanpa harus dijelaskan?").
pertanyaan(sendiri, "Apakah kamu lebih suka bekerja sendiri daripada dalam kelompok?").
pertanyaan(tak_sesuai_rencana, "Apakah kamu merasa sangat terganggu jika sesuatu berjalan tidak sesuai dengan rencana?").
pertanyaan(bosan, "Apakah kamu sering merasa bosan jika rutinitas tidak berubah?").
pertanyaan(hindari_konflik, "Apakah kamu sering menghindari konflik atau konfrontasi langsung?").
pertanyaan(sulit_percaya_orang, "Apakah kamu merasa sulit mempercayai orang lain pada awal perkenalan?").

% --------------------------
% INFERENSI & INTERAKSI
% --------------------------

% Reset jawaban sebelum memulai
reset_jawaban :- 
    retractall(sifat_pos(_)),
    retractall(sifat_neg(_)).

% Menampilkan semua pertanyaan ke pengguna
tanya_semua :-
    forall(pertanyaan(ID, Teks), (
        format("~w (y/n): ", [Teks]),
        read(Jawaban),
        (Jawaban == y -> assertz(sifat_pos(ID)) ; assertz(sifat_neg(ID)))
    )).

% Menentukan hasil akhir
evaluasi_kepribadian(TipeTerbaik) :-
    findall(Tipe, kepribadian(Tipe), SemuaTipe),
    hitung_skor(SemuaTipe, SkorList),
    pilih_tertinggi(SkorList, TipeTerbaik).

% Hitung jumlah sifat yang cocok untuk setiap kepribadian
hitung_skor([], []).
hitung_skor([Tipe|Rest], [(Tipe,Skor)|SkorList]) :-
    findall(Sifat, (sifat(Sifat, Tipe), sifat_pos(Sifat)), SifatCocok),
    length(SifatCocok, Skor),
    hitung_skor(Rest, SkorList).

% Pilih kepribadian dengan skor tertinggi
pilih_tertinggi([(Tipe, Skor)], Tipe) :- !.
pilih_tertinggi([(Tipe1, Skor1), (Tipe2, Skor2)|Rest], TipeTerbaik) :-
    (Skor1 >= Skor2 ->
        pilih_tertinggi([(Tipe1, Skor1)|Rest], TipeTerbaik)
    ;
        pilih_tertinggi([(Tipe2, Skor2)|Rest], TipeTerbaik)
    ).

# % Program utama
# mulai :-
#     reset_jawaban,
#     writeln("=== Tes Kepribadian Hewan ==="),
#     tanya_semua,
#     evaluasi_kepribadian(Hasil),
#     format("~nKepribadian kamu adalah: ~w~n", [Hasil]).
