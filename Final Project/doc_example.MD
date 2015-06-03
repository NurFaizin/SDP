# Link - Submit

REST Wrapper untuk tautan. Menyediakan metode untuk men-_submit_ tautan.

## URL
/tautan

## Methods
POST

## Data Params
- **title** [String] Judul tautan yang akan di-submit
- **link** [String] URL tautan

Contoh:
```
{
    title: "Great Works in Programming Languages",
    link: "http://www.cis.upenn.edu/~bcpierce/courses/670Fall04/GreatWorksInPL.shtml"
}
```

## Success Response
Jika sukses akan mengembalikan ID yang dimiliki oleh tautan yang baru di-_submit_.

```
HTTP/1.1 200 Success
{
    id: 12
}
```

## Error Response
### Code 401 Unauthorized
```
HTTP/1.1 401 Unauthorized
{
    message: "Log in"
}
```

### Code 422 Unprocessable Entry
```
HTTP/1.1 422 Unprocessable Entry
{
    message: "Link invalid"
}
```
