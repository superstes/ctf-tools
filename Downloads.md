# External Tools

## Sources

* Kali Debian Repository
  ```bash
  deb http://http.kali.org/kali kali-rolling main contrib non-free
  sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 ED444FF07D8D0BF6
  
  sudo nano /etc/apt/preferences.d/10-kali
  > Package: *
  > Pin-Priority: 1
  > Pin: origin http.kali.org
  ```

## File analysis

* binwalk
* exiftool

## Reverse Engineering

* Cutter => https://github.com/rizinorg/cutter
* ReClass.NET => https://github.com/ReClassNET/ReClass.NET

### Windows
* x64dbg => https://sourceforge.net/projects/x64dbg/files/snapshots/

## Stego
* Toolkit => https://github.com/DominicBreuker/stego-toolkit
  ```bash
  sudo docker pull dominicbreuker/stego-toolkit
  sudo docker run -it -v /home/superstes/Documents/ctfs/acsc23:/data dominicbreuker/stego-toolkit /bin/bash
  ```

* StegHide
* StegSeek => https://github.com/RickdeJager/stegseek (steghide cracking)

  ```bash
  stegseek img.jpg /usr/share/wordlists/rockyou.txt
  stegseek --seed img.jpg
  ```

* StegoVeritas => https://github.com/bannsec/stegoVeritas
* zsteg => https://github.com/zed-0xff/zsteg
* pdf-parser

  ```bash
  pdf-parser -c file.pdf

  # export object
  pdf-parser -o 30 -f -d obj30.bin file.pdf
  # export multiple objects
  for i in {1..35}; do pdf-parser -o $i -f -d "obj${i}.bin" file.pdf;done
  file obj*
  ```

* Decodify => https://github.com/UltimateHackers/Decodify
