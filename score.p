$( [Intro]
l = Eval(
	FileText(FileDir(GetAppName) + "\..\plWave\plWave.p"), 
	FileDir(GetAppName) + "\shm\shm.pi", "plWave" 
); l = l; 

ton _ 0.0;

len _ 2500;
tkt = len * 8 : 9;

fxl = "zsd"; pos = "sss"; pow = "aae"; 
bld = "" + fxl + " " + pos + " " + pow;

Mdl10SStr = l.layer(l, #, "Modd", len, ton, "1", "0", "S", #, 1.00);
Mdl10S _ Mdl10SStr.Wave; Mdl10SLen _ Mdl10SStr.Length;
Mdl579Str = l.layer(l, #, "Modd", len, ton, "5", "7", "9", #, 1.00);
Mdl579 _ Mdl579Str.Wave; Mdl579Len _ Mdl579Str.Length;
Mdl1duStr = l.layer(l, #, "Modd", len, ton, "1", "d", "u", #, 1.00);
Mdl1du _ Mdl1duStr.Wave; Mdl1duLen _ Mdl1duStr.Length;

Seq = seq
Smp = smp
Exp = exp
