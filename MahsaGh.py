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
            background: linear-gradient(135deg, #ffecd2, #fcb69f);
            font-family: 'Poppins', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 25px;
            padding: 30px;
            max-width: 600px;
            width: 100%;
        }
        .card {
            background: rgba(255, 255, 255, 0.25);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
            text-align: center;
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeIn 1s ease-in-out;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
        }
        .card h2 {
            color: #1f2f56;
            margin-bottom: 10px;
            font-size: 1.8em;
            font-weight: 600;
        }
        .card p {
            color: #3b3b3b;
            font-size: 1.3em;
            margin: 0;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @media (max-width: 600px) {
            .card {
                padding: 20px;
            }
            .card h2 {
                font-size: 1.5em;
            }
            .card p {
                font-size: 1.1em;
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
        <div class="card">
            <h2>CI/CD Status</h2>
            <p>CI/CD pipeline completed successfully!</p>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("index.html is created!")
