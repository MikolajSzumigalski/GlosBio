### Jak wszystko odpalić?  
Potrzebne są:  
* Python 3
* pipenv
* npm
*  [ffmpeg](http://ffmpeg.org) - dodany do PATH na systemie

#### API
wchodzimy w folder `Backend`
* odpalamy `python run.py` lub `pipenv install && pipenv run python main.py`
* cieszymy się postawionym serwerem na porcie 5000
* pliki .wav zapisywane są w folderze Backend/data
 
#### Aplikacja webowa
* wchodzimy w folder `frontend`
* odpalamy `npm install && npm run start`
* okno z apką wyskoczy samo w domyślnej przeglądarce

### Aplikacja mobilna (Android od wersji 4.4)
* wchodzimy do folderu `mobile`
* odpalamy `npm install`
* jeśli nie posiadamy telefonu z Androidem możemu uruchomić aplikację na [emulatorze](https://facebook.github.io/react-native/docs/getting-started)
* jeśli chcemy zainstalować aplikację na telefonie musimy połączyć się z komputerem przez USB i telefon musi być w trybie developerskim
* uruchamiamy aplikację przez `react-native run-android --variant=release` (należy pamętać, że to nie zadziała jeśli mamy już tą aplikację zainstalowaną na telefonie)
