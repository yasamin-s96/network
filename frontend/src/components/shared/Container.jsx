

const Container = ({ children, additionalClasses }) => {
    return (
        <div className={`h-screen bg-img bg-slate-950 bg-opacity-50 bg-blend-overlay bg-cover bg-center bg-no-repeat ${additionalClasses}`}>
            {children}
        </div>
    )
}

export default Container