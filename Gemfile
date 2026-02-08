# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "jekyll", "~> 4.4"
gem "jekyll-last-modified-at", git: "https://github.com/maximevaillancourt/jekyll-last-modified-at", branch: "add-support-for-files-in-git-submodules"
gem "webrick", "~> 1.9"
gem "nokogiri"

# 아래 부분이 추가되었습니다. 사이트맵을 만드는 플러그인을 설치합니다.
group :jekyll_plugins do
  gem "jekyll-sitemap"
end
