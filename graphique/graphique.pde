String[] lignes;
int numero;
String raccourci = "Desktop/pythonMail/verif.txt";

void setup(){ 
}

void draw(){
  lignes = loadStrings(raccourci);
  if(lignes.length != 0){
    numero = int(lignes[0]);
  }
  if(numero == 1){
      background(0, 255, 0);// un message !
  }
  else if(mousePressed && numero != 1){
    background(0);
  }
  println(lignes);
}