"""
Hikaru-Aegis Authentication Server

Controls the authentication process for Hikaru-Aegis

Default port: 8000
"""

if __name__ == '__main__':
    from server import app
    import uvicorn
    uvicorn.run(app)  # type: ignore
