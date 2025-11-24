import os

def get_auto_reply_template(name):
    # Use the public Vercel URL for optimal performance (caching, smaller email size)
    # Ensure the project is deployed to Vercel for this to appear.
    logo_src = os.getenv("LOGO_URL", "https://innovalabs.studio/logo_white.png")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Message Received</title>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
    </head>
    <body style="margin: 0; padding: 0; font-family: 'Montserrat', 'Segoe UI', sans-serif; background-color: #f4f4f5;">
        <table role="presentation" style="width: 100%; border-collapse: collapse;">
            <tr>
                <td align="center" style="padding: 40px 0;">
                    <table role="presentation" style="width: 600px; border-collapse: collapse; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <!-- Header -->
                        <tr>
                            <td style="background-color: #0f172a; padding: 30px 40px; text-align: center;">
                                <table role="presentation" style="width: 100%; border-collapse: collapse;">
                                    <tr>
                                        <td align="center">
                                            <img src="{logo_src}" alt="Logo" style="vertical-align: middle; max-width: 75px; height: auto; margin-right: 15px;">
                                            <span style="font-family: 'Montserrat', sans-serif; font-size: 32px; font-weight: 800; letter-spacing: -0.5px; vertical-align: middle;">
                                                <span style="color: #67e8f9;">INNOVA</span><span style="color: #ffffff;">SOFT</span>
                                            </span>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                        
                        <!-- Body -->
                        <tr>
                            <td style="padding: 40px;">
                                <h2 style="margin: 0 0 20px; color: #1e293b; font-size: 20px;">Hola {name},</h2>
                                <p style="margin: 0 0 20px; color: #475569; line-height: 1.6;">
                                    Gracias por contactar a <strong>InnovaSoft</strong>. Hemos recibido tu mensaje exitosamente y nuestro equipo ya lo está revisando.
                                </p>
                                <p style="margin: 0 0 30px; color: #475569; line-height: 1.6;">
                                    Nos especializamos en transformar negocios a través de IA Empresarial y software a medida diseñado para un impacto comercial real. Uno de nuestros expertos se pondrá en contacto contigo dentro de las próximas 24 horas para discutir cómo podemos ayudarte a alcanzar tus objetivos.
                                </p>
                                <div style="background-color: #f8fafc; border-left: 4px solid #06b6d4; padding: 15px; margin-bottom: 30px;">
                                    <p style="margin: 0; color: #64748b; font-size: 14px; font-style: italic;">
                                        "La innovación no es solo tecnología, es dar forma al futuro."
                                    </p>
                                </div>
                                <p style="margin: 0; color: #475569; line-height: 1.6;">
                                    Saludos cordiales,<br>
                                    <strong style="color: #0f172a;">El Equipo de InnovaSoft</strong>
                                </p>
                            </td>
                        </tr>
                        
                        <!-- Footer -->
                        <tr>
                            <td style="background-color: #f1f5f9; padding: 20px 40px; text-align: center;">
                                <p style="margin: 0; color: #94a3b8; font-size: 12px;">
                                    &copy; 2024 InnovaSoft. All rights reserved.<br>
                                    Arequipa, Peru
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
