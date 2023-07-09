# Proje Açıklaması

Bu proje, Google Cloud YouTube Data API'sini kullanarak belirli bir YouTube oynatma listesinin başlıklarını ve videolarını Markdown formatına dönüştürür.

## Kurulum

1. Python'u bilgisayarınıza kurun: [Python İndirme Sayfası](https://www.python.org/downloads/)
2. Bu projeyi klonlayın: `git clone https://github.com/kerim47/YT_playlist_to_md.git`
3. Gerekli Python paketlerini yüklemek için terminali açın ve proje dizinine gidin: `cd YT_playlist_to_md`
4. Gerekli paketleri yüklemek için aşağıdaki komutu çalıştırın: `pip install -r requirements.txt`

## Kullanım

1. `config.toml` dosyasını açın ve aşağıdaki bilgileri doldurun:
   - `playlist_id`: YouTube oynatma listesi kimliği
   - `api_key`: YouTube Data API'si için API anahtarınız
   - `path`: Markdown dosyasının kaydedileceği dizin yolu

2. `main.py` dosyasını çalıştırarak YouTube oynatma listesinin başlıklarını ve videolarını Markdown formatına dönüştürün: `python main.py`

3. Markdown dosyası belirlediğiniz `path` dizinine kaydedilecektir.

## Gereksinimler

- Python 3.x
- `toml` paketi
- `requests` paketi

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
