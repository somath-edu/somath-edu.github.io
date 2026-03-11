#!/bin/bash
echo "=== GitHub 업로드 ==="
read -s -p "🔑 새 토큰 붙여넣기 (입력해도 화면에 안 보임): " TOKEN
echo ""
git push https://somath-edu:$TOKEN@github.com/somath-edu/somath-edu.github.io.git main
echo "✅ 완료!"
