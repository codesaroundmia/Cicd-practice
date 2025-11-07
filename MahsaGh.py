
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Page</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #74ebd5, #acb6e5);
            font-family: 'Poppins', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            padding: 20px;
            max-width: 600px;
            width: 100%;
        }
        .card {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeIn 1s ease-in-out;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);
        }
        .card h2 {
            color: #2c3e50;
            margin: 0;
            font-size: 1.8em;
            font-weight: 600;
        }
        .card p {
            color: #34495e;
            font-size: 1.4em;
            margin: 10px 0 0;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @media (max-width: 600px) {
            .card {
                padding: 15px;
            }
            .card h2 {
                font-size: 1.5em;
            }
            .card p {
                font-size: 1.2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <h2>Name</h2>
            <p>Mahsa Ghazaghi</p>
        </div>
        <div class="card">
            <h2>Student ID</h2>
            <p>40113011016</p>
        </div>
    </div>

<!-- تست دیپلوی  [2025-11-07-v2] -->
    <p style="text-align:center; color:#2c3e50;">Deployment Test v2.0 - 2025/11/07</p>
</body>
</html>
"""


with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("index.html is created!")



