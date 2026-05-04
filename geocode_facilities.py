import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# --- Paths ---
csv_in  = r"D:\bakhuongcao\Statpub\VN_map\Health faclities\Co-so-KCB-ban-dau-2026.csv"
csv_out = r"D:\bakhuongcao\Statpub\VN_map\Health faclities\Co-so-KCB-ban-dau-2026_geocoded.csv"

# --- Load data ---
df = pd.read_csv(csv_in, encoding="utf-8-sig")
address_col = "Địa chỉ"

# --- Geocoder setup (Nominatim requires a unique user_agent) ---
geolocator = Nominatim(user_agent="vn_health_facilities_geocoder", timeout=10)

def geocode(address):
    """Return (lat, lon) or (None, None) if not found."""
    try:
        # Append Vietnam to improve accuracy
        location = geolocator.geocode(str(address) + ", Việt Nam")
        if location:
            return location.latitude, location.longitude
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"  Error: {e}")
    return None, None

# --- Geocode each row ---
latitudes, longitudes = [], []
total = len(df)

for i, row in df.iterrows():
    address = row[address_col]
    lat, lon = geocode(address)
    latitudes.append(lat)
    longitudes.append(lon)
    status = f"({lat:.5f}, {lon:.5f})" if lat else "NOT FOUND"
    print(f"[{i+1}/{total}] {row['Tên Cơ sở khám chữa bệnh'][:50]} → {status}")
    time.sleep(1)  # Nominatim rate limit: max 1 request/second

df["latitude"]  = latitudes
df["longitude"] = longitudes

# --- Save output ---
df.to_csv(csv_out, index=False, encoding="utf-8-sig")
print(f"\nDone! Geocoded CSV saved to:\n{csv_out}")
found = df["latitude"].notna().sum()
print(f"Geocoded: {found}/{total} addresses found.")
