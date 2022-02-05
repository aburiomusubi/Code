def aburi_omusubi(omu,kome,nori):
  for i in range(omu):
    if kome[i] == "aburi" and nori[i] == "aburi":
      print("aburi_omusubi")
    elif kome[i] == "normal" and nori[i] == "normal":
      print("omusubi")
    else:
      print("half_aburi_omusubi")

omu = int(input())
kome = list(map(str,input().split()))
nori = list(map(str,input().split()))
aburi_omusubi(omu,kome,nori)

