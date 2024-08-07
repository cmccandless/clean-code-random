from dataclasses import dataclass
import re
from typing import List


RGX_CHAPTER = re.compile(r"^##\s*(?P<name>.*)$")
RGX_PHRASE = re.compile(r"^\d+\.\s*(?P<phrase>.*)$")


@dataclass
class Chapter:
    title: str
    number: int
    phrases: List[str]


@dataclass
class Book:
    name: str
    chapters: List[Chapter]

    @classmethod
    def from_md(cls, name: str, text: str) -> "Book":
        chapters = []
        chapter = None
        chapter_num = 0
        for line in text.splitlines():
            line = line.strip()
            if (m := RGX_CHAPTER.match(line)) is not None:
                chapter_num += 1
                chapter = Chapter(m.group("name"), chapter_num, [])
                chapters.append(chapter)
            elif (m := RGX_PHRASE.match(line)) is not None:
                chapter.phrases.append(m.group("phrase"))
        return cls(name, chapters)

    def get_chapter(self, chapter_num: str) -> Chapter:
        return self.chapters[chapter_num - 1]
    
    def get_phrases(self) -> List[str]:
        return [
            phrase
            for chapter in self.chapters
            for phrase in chapter.phrases
        ]
